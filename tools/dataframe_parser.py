import pandas as pd
def price_slippage_data_to_dataframe(data,type):
    processed_data = []
    for item in data:
        if item["data"].get("type")!=type:
            continue
        # Exclude transactions from the initial flattening process
        flattened_data = {
            "id": item.get("id"),
            "timestamp": item.get("timestamp"),
            "url": item["data"].get("url"),
            "plan": item["data"].get("plan"),
            "type": item["data"].get("type"),
            "network_value": item["data"]["network"].get("value"),
            "trigger": item["data"].get("trigger"),
            "severity": item["data"].get("severity"),
            "data_timestamp_value": item["data"]["timestamp"].get("value"),
            "data_timestamp_displayValue": item["data"]["timestamp"].get("displayValue"),
            "tokenSymbol_value": item["data"]["tokenSymbol"].get("value"),
            "tokenAddress_href": item["data"]["tokenAddress"].get("href"),
            "tokenAddress_value": item["data"]["tokenAddress"].get("value"),
            "liquidityPair_href": item["data"]["liquidityPair"].get("href"),
            "liquidityPair_value": item["data"]["liquidityPair"].get("value"),
            "liquidityValue_unit": item["data"]["liquidityValue"].get("unit"),
            "liquidityValue_value": item["data"]["liquidityValue"].get("value"),
            "slippagePercentage_value": item["data"]["slippagePercentage"].get("value"),
            # Add transactions as a single column containing the list of transactions
            "transactions": item["data"].get("transactions", [])
        }
        
        processed_data.append(flattened_data)

    return pd.DataFrame(processed_data)
def whale_movement_data_to_dataframe(data,type):
    processed_data = []
    for item in data:
        if item["data"].get("type")!=type:
            continue

        # Exclude transactions from the initial flattening process
        flattened_data = {
            "id": item.get("id"),
            "timestamp": item.get("timestamp"),
            "url": item["data"].get("url"),
            "plan": item["data"].get("plan"),
            "type": item["data"].get("type"),
            "network_value": item["data"]["network"].get("value"),
            "trigger": item["data"].get("trigger"),
            "severity": item["data"].get("severity"),
            "data_timestamp_value": item["data"]["timestamp"].get("value"),
            "data_timestamp_displayValue": item["data"]["timestamp"].get("displayValue"),
            "whaleName_value": item["data"]["whaleName"].get("value"),
            "whaleAddress_href": item["data"]["whaleAddress"].get("href"),
            "whaleAddress_value": item["data"]["whaleAddress"].get("value"),
            "tokenSymbol_value": item["data"]["tokenSymbol"].get("value"),
            "tokenAddress_href": item["data"]["tokenAddress"].get("href"),
            "tokenAddress_value": item["data"]["tokenAddress"].get("value"),
            "valueInUsd_unit": item["data"]["valueInUsd"].get("unit"),
            "valueInUsd_value": item["data"]["valueInUsd"].get("value"),
            "tokenAmount_value": item["data"]["tokenAmount"].get("value"),
            # Add transactions as a single column containing the list of transactions
            "transaction_href": item["data"]["transaction"].get("href"),
            "transaction_value": item["data"]["transaction"].get("value")
        }
        
        processed_data.append(flattened_data)

    return pd.DataFrame(processed_data)
def proxy_upgrade_data_to_dataframe(data,type):
    processed_data = []
    for item in data:
        if item["data"].get("type")!=type:
            continue
        # Exclude transactions from the initial flattening process
        flattened_data = {
            "id": item.get("id"),
            "timestamp": item.get("timestamp"),
            "url": item["data"].get("url"),
            "plan": item["data"].get("plan"),
            "type": item["data"].get("type"),
            "network_value": item["data"]["network"].get("value"),
            "trigger": item["data"].get("trigger"),
            "severity": item["data"].get("severity"),
            "data_timestamp_value": item["data"]["timestamp"].get("value"),
            "data_timestamp_displayValue": item["data"]["timestamp"].get("displayValue"),
            "address_href": item["data"]["address"].get("href"),
            "address_value": item["data"]["address"].get("value"),
            "newAddress_href": item["data"]["newAddress"].get("href"),
            "newAddress_value": item["data"]["newAddress"].get("value"),
            "tokenSymbol_value": item["data"]["tokenSymbol"].get("value")
        }
        
        processed_data.append(flattened_data)

    return pd.DataFrame(processed_data)
def large_liquidity_removal_data_to_dataframe(data,type):
    processed_data = []
    for item in data:
        if item["data"].get("type")!=type:
            continue
        # Exclude transactions from the initial flattening process
        flattened_data = {
            "id": item.get("id"),
            "timestamp": item.get("timestamp"),
            "url": item["data"].get("url"),
            "plan": item["data"].get("plan"),
            "type": item["data"].get("type"),
            "network_value": item["data"]["network"].get("value"),
            "trigger": item["data"].get("trigger"),
            "severity": item["data"].get("severity"),
            "data_timestamp_value": item["data"]["timestamp"].get("value"),
            "data_timestamp_displayValue": item["data"]["timestamp"].get("displayValue"),
            "transaction_href": item["data"]["transaction"].get("href"),
            "transaction_value": item["data"]["transaction"].get("value"),
            "removalValue_unit": item["data"]["removalValue"].get("unit"),
            "removalValue_value": item["data"]["removalValue"].get("value"),
            "senderAddress_href": item["data"]["senderAddress"].get("href"),
            "senderAddress_value": item["data"]["senderAddress"].get("value"),
            "token0Address_href": item["data"]["token0Address"].get("href"),
            "token0Address_value": item["data"]["token0Address"].get("value"),
            "token1Address_href": item["data"]["token1Address"].get("href"),
            "token1Address_value": item["data"]["token1Address"].get("value"),
            "liquidityValue_unit": item["data"]["liquidityValue"].get("unit"),
            "liquidityValue_value": item["data"]["liquidityValue"].get("value"),
            "liquidityAddress_href": item["data"]["liquidityAddress"].get("href"),
            "liquidityAddress_value": item["data"]["liquidityAddress"].get("value")
        }
        
        processed_data.append(flattened_data)

    return pd.DataFrame(processed_data)
def erc20_token_mint_or_burn_data_to_dataframe(data,type):
    processed_data = []
    for item in data:
        if item["data"].get("type")!=type:
            continue
        # Exclude transactions from the initial flattening process
        flattened_data = {
            "id": item.get("id"),
            "timestamp": item.get("timestamp"),
            "url": item["data"].get("url"),
            "plan": item["data"].get("plan"),
            "type": item["data"].get("type"),
            "network_value": item["data"]["network"].get("value"),
            "trigger": item["data"].get("trigger"),
            "severity": item["data"].get("severity"),
            "data_timestamp_value": item["data"]["timestamp"].get("value"),
            "data_timestamp_displayValue": item["data"]["timestamp"].get("displayValue"),
            "valueInUsd_unit": item["data"]["valueInUsd"].get("unit"),
            "valueInUsd_value": item["data"]["valueInUsd"].get("value"),
            "tokenAmount_value": item["data"]["tokenAmount"].get("value"),
            "tokenSymbol_value": item["data"]["tokenSymbol"].get("value"),
            "tokenAddress_href": item["data"]["tokenAddress"].get("href"),
            "tokenAddress_value": item["data"]["tokenAddress"].get("value"),
            "transactions": item["data"].get("transactions", [])
        }
        
        processed_data.append(flattened_data)

def attack_data_to_dataframe(data):
    processed_data=[]
    for item in data['data']:
        flattened_data = {
            "id": item.get("id"),
            "createdAt": item.get("createdAt"),
            "updatedAt": item.get("updatedAt"),
            "title": item.get("title"),
            "attackTime": item.get("attackTime"),
            "meta": item.get("meta"),
            "chainSlug": item.get("chainSlug"),
            "mwe": item.get("mwe"),
            "description": item.get("description"),
            "poc": item.get("poc"),
            "totalLossUsd": item.get("totalLossUsd"),
            "lossUsd": item.get("lossUsd"),
            "lossTokenSymbol": item.get("lossTokenSymbol"),
            "lossTokenAmount": item.get("lossTokenAmount"),
            "transactions": item.get("transactions"),
            "messageIds": item.get("messageIds"),
            "projectId": item.get("projectId"),
            "state": item.get("state"),
            "confirmedAt": item.get("confirmedAt"),
            "confirmedBy": item.get("confirmedBy"),
            "archived": item.get("archived"),
            "archivedAt": item.get("archivedAt"),
            "addressMappings": item.get("addressMappings"),
            "posts": item.get("posts")
        }
        processed_data.append(flattened_data)
    return pd.DataFrame(processed_data)
