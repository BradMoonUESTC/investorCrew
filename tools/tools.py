import json
import os
from fuzzywuzzy import fuzz
import requests
from crawler import Crawler
import pandas as pd
import tools.dataframe_parser as dataframe_parser
from crewai_tools import tool
class Web3EventLoader(object):
    api_key = ""
    state_file = os.getenv("STATE_FILE", "_web3_state")

    def __init__(self) -> None:
        self.state = {
            "posts": [
            ], 
            "events": [
            ],
            "last_id": 0,
        }
        if os.path.exists(self.state_file):
            self.state = os.pickle.load(open(self.state_file, "rb"))

    def load_events(self,**kwargs):
        """
        Load events with flexible querying capabilities.
        - day: Specify a day to filter events by timestamp.
        - limit: Limit the number of events returned.
        - types: Filter events by specific types.
        - severity: Filter events by severity level.
        - addresses: Filter events that involve specific addresses.
        """
        trigger = kwargs.get('trigger', "")
        limit = kwargs.get('limit', None)
        type = kwargs.get('type', None)
        severity = kwargs.get('severity', None)
        query_string = kwargs.get('query_string', "")
        query_fuzzy_string = kwargs.get('query_fuzzy_string', "")
        events = self._get_events_from_source(trigger)
        filtered_events = self._filter_events(events, type, severity, trigger,limit,query_string, query_fuzzy_string)

        return filtered_events
    
    def _get_events_from_source(self,trigger=""):
        return self._get_scout_events(trigger)
        
    def _get_scout_events(self,trigger=""):
        # 设置API的URL和API密钥
        url = f"https://v.meta001.net/api/metascout/alerts?trigger={trigger}"

        # 设置请求的Headers
        headers = {
            "X-API-Key": self.api_key,
        }

        # 发送GET请求
        response = requests.get(url, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            # 请求成功，打印响应的内容
            print("Success:")
            # print(response.text)
        else:
            # 请求失败，打印错误信息
            print("Error:", response.status_code)
            # print(response.text)
        
        events = response.text
        return events
    def _filter_events(self, events, type, severity=None, trigger="", limit=10,query_string="", query_fuzzy_string=""):
        filtered = json.loads(events)
        if type=="Price Slippage":
            dataframe=dataframe_parser.price_slippage_data_to_dataframe(filtered,type)
        elif type=="Whale Movement":
            dataframe=dataframe_parser.whale_movement_data_to_dataframe(filtered,type)
        elif type=="Proxy Upgrade":
            dataframe=dataframe_parser.proxy_upgrade_data_to_dataframe(filtered,type)
        elif type=="Large Liquidity Removal":
            dataframe=dataframe_parser.large_liquidity_removal_data_to_dataframe(filtered,type)
        elif type=="ERC20 Token Mint or Burn":
            dataframe=dataframe_parser.erc20_token_mint_or_burn_data_to_dataframe(filtered,type)
        # Filter by severity if specified
        if severity:
            dataframe = dataframe[dataframe['severity'].isin(severity)]

        # Filter by trigger if specified
        if trigger:
            dataframe = dataframe[dataframe['trigger'] == trigger]

        # Filter by limit if specified
        if limit:
            dataframe = dataframe.head(limit)
        
        # 根据query_string中定义的属性进行精准匹配
        # query_string = {
        #     "type": "Price Slippage",
        #     "severity": "HIGH",
        #     "trigger": "PriceSlippageETH"
        # }
        if query_string!="":
            for key, value in query_string.items():
                dataframe = dataframe.loc[dataframe[key] == value]
        if query_fuzzy_string!="":
            for key, value in query_fuzzy_string.items():
                dataframe = dataframe[key].apply(lambda x: fuzz.ratio(x, value)) > 80
        # Convert filtered DataFrame back to JSON format
        return dataframe.to_dict(orient='records')
    
    def dump(self, event):
        
        event = json.loads(event['data'])

        network = event['network']['value']
        time = event['timestamp']['displayValue']
        event_type = event['type']

        if event_type == 'Large Liquidity Removal':
            try:
                liqudity = "%.0f %s" % (event['liquidityValue']['value'], event['liquidityValue']['unit'])
                removal = "%.0f %s" % (event['removalValue']['value'], event['removalValue']['unit'])
                senderAddress = event['senderAddress']['value']
                token0Address = event['token0Address']['value']
                token1Address = event['token1Address']['value']
                
                msg = f"{senderAddress} removed {removal} from liqudity pool with pair of {token0Address} and {token1Address}, the liquidity value involved was {liqudity}"
            except Exception as e:
                print("failed to parse ", json.dumps(event))
                msg = None 
            
        elif event_type == 'Whale Movement':
            whaleAddress = event['whaleAddress']['value']
            whaleName = event['whaleName']['value']
            tokenAddress = event['tokenAddress']['value']
            tokenSymbol = event['tokenSymbol']['value']
            value = event['valueInUsd']['value']

            # The whale address involved is 0xa180fe01b906a1be37be6c534a3300785b20d947, known as 'Binance: Hot Wallet 16.' The transaction, identified as 0x280ae618de4b6929e5be4fdf91dc917268ddb009e1d17d6509eaefa941a14f81, involved a token amount of 3,052,606.24 USDT, with a total value of $3,049,701.66 USD. 
            # msg = '%s removed %.0f from liqudity pool with pair of %s and %s, the liquidity value involved was %.0f' % (senderAddress, removal, token0Address, token1Address, liqudity)
            # https://bscscan.com/tx/0xd2bb86b78dfbc2b092edeb0645f61b5b286d31e4fd7eb1a659179970c21ffe03
            # msg = 'The whale address involved is %s, known as %s. The transaction, involved a token amount of %.2f %s, with a total value of $%.2f USD.' % (whaleAddress, whaleName, value, tokenSymbol, value)
            msg = None
        elif event_type == 'Price Slippage':
            # a high-severity price slippage event occurred on the Binance Smart Chain (BSC) involving the THOREUM token. The slippage percentage was 64.05%, impacting a liquidity value of $1,017,822.29 USD. The specific token address is 0xce1b3e5087e8215876af976032382dd338cf8401, and the liquidity pair can be traced to 0xd822e1737b1180f72368b2a9eb2de22805b67e34.
            tokenAddress = event['tokenAddress']['value']
            tokenSymbol = event['tokenSymbol']['value']
            slippage = event['slippagePercentage']['value']
            liquidityValue = event['liquidityValue']['value']
            msg = f'''a price slippage event occurred on the {network} involving the {tokenSymbol} token. The slippage percentage was {slippage}, impacting a liquidity value of {liquidityValue} USD. The specific token address is {tokenAddress}'''
    
        if msg is None:
            return None
        
        return f'''[{time}] {msg}'''



if __name__ == "__main__":
#   events_loader = Web3EventLoader()
    # cralwer=Crawler("https://app.trendx.tech/smartMoney/signal")
    # res=cralwer.extract_root_divs_without_svg()
    # print(res)
    loader = Web3EventLoader()
    print(loader._get_twitter_search("merlin"))
#   events = events_loader.load_day_events("15 Feb")
#   event_briefs = [events_loader.dump(x) for x in events]
#   event_briefs = list(filter(lambda x: x is not None, event_briefs))
#   es = ["- " + x for x in event_briefs]
#   print("\n".join(es))

    # loader = Web3EventLoader()
    # events = loader.load_events(day="15 Feb", limit=5, types=["Large Liquidity Removal", "Price Slippage"], severity=["HIGH", "MEDIUM"],addresses=["0x52dddfe46bb5dc27586fb0fd4d44c839032b5b1f"])
    # print(events)