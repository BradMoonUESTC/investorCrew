import json
import os
import dotenv
import requests

dotenv.load_dotenv()

from crew.crew import Web3SecurityCrew
from tools.tools import Web3EventLoader
# config_batch="config_large_liquidity_removal"
# config_ = getattr(config, config_batch)
from utilities.crew_config import config_analysis_hidden_action_from_event as config

loader = Web3EventLoader()
# twitter_search_query = config["twitter_search_keyword"]
# if twitter_search_query !="":
#     query_result=loader._get_twitter_search(twitter_search_query)
#     # 更新 config 中的 params，使其引用 state 中的正确键
#     loader.state['twitter_infos'] = query_result
#     for task in config['tasks']:
#         task['params'] = {k: v for k, v in task['params'].items()}
    
#     crew = Web3SecurityCrew(config)
#     r = crew.kickoff(loader.state)
if "event_loader_params" in config:
    event_loader_params = config['event_loader_params']

    if len(event_loader_params)==0:
        # 更新 config 中的 params，使其引用 state 中的正确键
        for task in config['tasks']:
            task['params'] = {k: v for k, v in task['params'].items()}
        
        crew = Web3SecurityCrew(config)
        r = crew.kickoff(loader.state)
    else:
        events = loader.load_events(**event_loader_params)
        print(events)
        if len(events) > 0:
            loader.state['events'] = events
            # 更新 config 中的 params，使其引用 state 中的正确键
            for task in config['tasks']:
                task['params'] = {k: v for k, v in task['params'].items()}
            
            crew = Web3SecurityCrew(config)
            r = crew.kickoff(loader.state)

            loader.state['last_id'] = events[-1]['id']

            print(r)
