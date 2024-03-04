import json
import os
import dotenv
import requests

dotenv.load_dotenv()

from crew.crew import Web3SecurityCrew
from tools import Web3EventLoader
# config_batch="config_large_liquidity_removal"
# config_ = getattr(config, config_batch)
from config.config import config_decompose_input_text_to_params_and_brief as config

loader = Web3EventLoader()
input_text="我想知道一下最近2天的涉及到的eth链的攻击事件"
config['tasks'][0]['params']['input_text'] = input_text
for task in config['tasks']:
    task['params'] = {k: v for k, v in task['params'].items()}

crew = Web3SecurityCrew(config)
r = crew.kickoff(loader.state)

# if "event_loader_params" in config:
#     event_loader_params = config['event_loader_params']

#     if len(event_loader_params)==0:
#         # 更新 config 中的 params，使其引用 state 中的正确键
#         for task in config['tasks']:
#             task['params'] = {k: v for k, v in task['params'].items()}
        
#         crew = Web3SecurityCrew(config)
#         r = crew.kickoff(loader.state)
#     else:
#         events = loader.load_events(**event_loader_params)
#         # print(events)
#         if len(events) > 0:
#             loader.state['events'] = events
#             # 更新 config 中的 params，使其引用 state 中的正确键
#             for task in config['tasks']:
#                 task['params'] = {k: v for k, v in task['params'].items()}
            
#             crew = Web3SecurityCrew(config)
#             r = crew.kickoff(loader.state)
            
#             loader.state['last_id'] = events[-1]['id']

#             # print(r)
