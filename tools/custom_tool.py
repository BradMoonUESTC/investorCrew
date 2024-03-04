from datetime import datetime
import json
from crewai_tools import BaseTool
import pandas as pd
import requests
import tools.dataframe_parser as dataframe_parser
from fuzzywuzzy import fuzz

class TwitterTool(BaseTool):
    name: str = "TwitterTool"
    description: str = "This tool is used to get the latest information about a project from Twitter."

    def _run(tool_input: str) -> str:
        print("From TwitterTool itself——twitter search key word:",tool_input)
        # Implementation goes here
        api_key = "f106d97f8b3782f83fa2d2ffa2cc0493"
        # 设置API的URL和API密钥
        url = f"https://v.meta001.net/api/twitter/search?query={tool_input}"

        # 设置请求的Headers
        headers = {
            "X-API-Key": api_key,
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
        
        tweets = response.text
        return tweets
        # pass
    
class EventTool(BaseTool):
    name: str = "EventTool"
    description: str = "This tool is used to get the latest events from a project."

    def _run(limit:str,time_start:str,time_end:str,type:str,query_string: str) -> str:
        # trigger = tool_input_json.get('trigger', "")

        # 根据用户输入进行单工具分支处理，引流到attack中
        if type=="attack":
            print("检测到用户的攻击查询请求，引流到AttackTool中")
            return AttackTool._run(limit,time_start,time_end,query_string)
        
        trigger=""
        severity = None
        query_fuzzy_string=""
        # severity = tool_input_json.get('severity', None)
        # query_string = tool_input_json.get('query_string', "")
        # query_fuzzy_string = tool_input_json.get('query_fuzzy_string', "")
        events = EventTool._get_events_from_source(trigger)
        filtered_events = EventTool._filter_events(events, type, time_start,time_end,severity, trigger,limit,query_string, query_fuzzy_string)
        return filtered_events
    def _get_events_from_source(trigger=""):
        return EventTool._get_scout_events(trigger)
        
    def _get_scout_events(trigger=""):
        # 设置API的URL和API密钥
        api_key="f106d97f8b3782f83fa2d2ffa2cc0493"
        url = f"https://v.meta001.net/api/metascout/alerts?trigger={trigger}"

        # 设置请求的Headers
        headers = {
            "X-API-Key": api_key,
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
    def _filter_events( events, type, time_start,time_end,severity=None, trigger="", limit=10,query_string="", query_fuzzy_string=""):
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
        # if severity:
        #     dataframe = dataframe[dataframe['severity'].isin(severity)]

        # Filter by trigger if specified
        if trigger:
            dataframe = dataframe[dataframe['trigger'] == trigger]
        if time_start:
            time_start = datetime.fromisoformat(time_start.rstrip('Z'))  # 移除尾部的'Z'（如果有的话）并解析
        if time_end:
            time_end = datetime.fromisoformat(time_end.rstrip('Z'))  # 移除尾部的'Z'（如果有的话）并解析

        # 然后，对DataFrame中的每个日期时间字符串进行同样的解析处理，并进行比较
        if time_start:
            dataframe = dataframe[pd.to_datetime(dataframe['data_timestamp_displayValue']).gt(time_start)]
        if time_end:
            dataframe = dataframe[pd.to_datetime(dataframe['data_timestamp_displayValue']).lt(time_end)]        # Filter by limit if specified
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
class AttackTool(BaseTool):
    name: str = "AttackTool"
    description: str = "This tool is used to get the latest attacks from a project."

    def _run(limit:str,time_start:str,time_end:str,query_string:str) -> str:
        attacks = AttackTool._get_attacks()
        filtered_attacks = AttackTool._filter_attacks(attacks,limit,time_start,time_end,query_string)
        return filtered_attacks
        
        
    def _get_attacks():
        # 设置API的URL和API密钥
        api_key="f106d97f8b3782f83fa2d2ffa2cc0493"
        url = f"https://v.meta001.net/api/attack/list?pageSize=1300"

        # 设置请求的Headers
        headers = {
            "X-API-Key": api_key,
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
        
        attacks = response.text
        return attacks
    def _filter_attacks(attacks,limit,time_start,time_end,query_string=""):        
        filtered = json.loads(attacks)
        print("开始解析攻击数据")
        dataframe=dataframe_parser.attack_data_to_dataframe(filtered)
        dataframe = dataframe[~dataframe['title'].str.contains("suspected attack module", na=False)]
        if time_start:
            time_start = datetime.fromisoformat(time_start.rstrip('Z'))  # 移除尾部的'Z'（如果有的话）并解析
        if time_end:
            time_end = datetime.fromisoformat(time_end.rstrip('Z'))  # 移除尾部的'Z'（如果有的话）并解析

        # 然后，对DataFrame中的每个日期时间字符串进行同样的解析处理，并进行比较
        if time_start:
            dataframe = dataframe[pd.to_datetime(dataframe['attackTime']).gt(time_start)]
        if time_end:
            dataframe = dataframe[pd.to_datetime(dataframe['attackTime']).lt(time_end)]        # Filter by limit if specified
        if query_string!="":
            for key, value in query_string.items():
                dataframe = dataframe.loc[dataframe[key] == value]

        if limit:
            dataframe = dataframe.head(limit)

        print("解析攻击数据完成")
        return dataframe.to_dict(orient='records')