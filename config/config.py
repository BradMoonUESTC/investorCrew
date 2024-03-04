# config使用方法：
# 先定义agents，然后定义tasks，tasks中的agent指向agents中的agent
# agents中的方法名对应的是agents.py中的方法名
# tasks中的name对应的是tasks.py中的方法名
# params中的对应的是tasks.py中的方法的参数名
config_liquidity_removal_twitter = {
    "event_loader_params": {
        "limit": 5,
        "type": "Large Liquidity Removal",
        "severity": ["HIGH", "MEDIUM"]
    },
    "agents": {
        "basic_analyzer_for_token_removal": "basic_analyzer_for_token_removal_agent",
        "basic_writer_for_twitter": "basic_writer_for_twitter_agent"
    },
    "tasks": [
        {
            "name": "liquidity_removal_explain_task",
            "agent": "basic_analyzer_for_token_removal",
            "params": {
                "posted": "posts",  # 注意这里将直接使用 state 中的 key
                "events": "events"  # 同上
            }
        },
        {
            "name": "basic_twitter_send_task",
            "agent": "basic_writer_for_twitter",
            "params": {
            }
        }
    ]
}

config_whale_movement_twitter_bsc= {
    "event_loader_params": {
        "limit": 10,
        "type": "Whale Movement",
        "severity": ["HIGH"],
        "whaleName":"Binance: Hot Wallet"#模糊搜索
    },
    "agents": {
        "whale_movement_analyzer": "whale_movement_analysis_agent",
        "social_media_poster": "basic_writer_for_twitter_agent"
    },
    "tasks": [
        # task作用：解读最近的大额资金转移活动，并发布推文
        {
            "name": "analyze_whale_movement_event_task",
            "agent": "whale_movement_analyzer",
            "params": {
                "events": "events" # 名称events必须是对应方法的参数名，后面的events无所谓，会替换
            }
        },
        {
            "name": "basic_twitter_send_task",
            "agent": "social_media_poster",
            "params": {
            }
        }
    ]
}
# Whale Movement 事件处理配置
# 配置说明：
# - event_loader_params: 事件加载器参数，用于加载事件数据
# - agents: 事件处理相关的 agent 配置
# - tasks: 事件处理相关的任务配置
config_whale_movement_twitter = {
    "event_loader_params": {
        "limit": 10,
        "type": "Whale Movement",
        "trigger":"WhaleMovementBSC"
    },
    "agents": {
        "whale_movement_analyzer": "whale_movement_analysis_agent",
        "social_media_poster": "basic_writer_for_twitter_agent"
    },
    "tasks": [
        # task作用：解读最近的大额资金转移活动，并发布推文
        {
            "name": "analyze_whale_movement_event_task",
            "agent": "whale_movement_analyzer",
            "params": {
                "events": "events" # 名称events必须是对应方法的参数名，后面的events无所谓，会替换
            }
        },
        {
            "name": "basic_twitter_send_task",
            "agent": "social_media_poster",
            "params": {
            }
        }
    ]
}

#流动性移除事件分析反应分析配置
config_liquidity_removal_reaction_twitter = {
    "event_loader_params": {
        "limit": 10,
        "type": "Large Liquidity Removal",
        "severity": ["HIGH", "MEDIUM"]
    },
    "agents": {
        "basic_analyzer_for_token_removal": "basic_analyzer_for_token_removal_agent",
        "market_trend_analysis": "market_trend_analysis_agent"
    },
    "tasks": [
        {
            "name": "liquidity_removal_explain_task",
            "agent": "basic_analyzer_for_token_removal",
            "params": {
                "posted": "posts",  # 注意这里将直接使用 state 中的 key
                "events": "events"  # 同上
            }
        },
        {
            "name": "predict_market_response_task",
            "agent": "market_trend_analysis",
            "params": {
            }
        }
    ]
}

config_analysis_hidden_action_from_event = {
    "event_loader_params": {
        "limit": 10,
        "type": "Large Liquidity Removal",
        "severity": ["HIGH", "MEDIUM"]
    },
    "agents": {
        "brief":"brief_agent",
        "market_action_analysis":"market_action_analysis_agent"
    },
    "tasks": [
        {
            "name": "brief_the_event_task",
            "agent": "brief",
            "params": {
                "events": "events"
            }
        },
        {
            "name": "hidden_action_analysis_task",
            "agent": "market_action_analysis",
            "params": {
            }
        }
    ]
}

config_analysis_hidden_action_from_liquidity_removal_with_tweet = {
    "event_loader_params": {
        "limit": 10,
        "type": "Large Liquidity Removal",
        "severity": ["HIGH", "MEDIUM"],
    },
    "agents": {
        "brief":"brief_agent",
        "market_action_analysis":"market_action_analysis_agent",
        "social_media_poster": "basic_writer_for_twitter_agent"

    },
    "tasks": [
        {
            "name": "brief_the_event_task",
            "agent": "brief",
            "params": {
                "events": "events"
            }
        },
        {
            "name": "hidden_action_analysis_task",
            "agent": "market_action_analysis",
            "params": {
            }
        },
        {
            "name": "basic_twitter_send_task",
            "agent": "social_media_poster",
            "params": {
            }
        }

    ]
}

config_analysis_hidden_action_from_whale_movement_with_tweet = {
    "event_loader_params": {
        "limit": 10,
        "type": "Whale Movement",
        "severity": ["HIGH", "MEDIUM"],
        "whaleName":"Binance: Hot Wallet"#模糊搜索
    },
    "agents": {
        "brief":"brief_agent",
        "market_action_analysis":"market_action_analysis_agent",
        "social_media_poster": "basic_writer_for_twitter_agent"

    },
    "tasks": [
        {
            "name": "brief_the_event_task",
            "agent": "brief",
            "params": {
                "events": "events"
            }
        },
        {
            "name": "hidden_action_analysis_task",
            "agent": "market_action_analysis",
            "params": {
            }
        },
        {
            "name": "basic_twitter_send_task",
            "agent": "social_media_poster",
            "params": {
            }
        }

    ]
}

config_investor_for_new_project = {
    "event_loader_params": {
        
    },
    "agents": {
        "twitter_searcher":"twitter_searcher_agent",
        # "new_project_analyzer":"new_project_analyzer_agent"
        },
    "tasks": [
        {
            "name": "twitter_deep_search_keyword_task",
            "agent": "twitter_searcher",
            "params": {
                "project_name": "manta network"
            }
        },
        {
            "name":"twitter_search_info_task",
            "agent":"twitter_searcher",
            "params":{
            }
        }
    ]
}

config_investor_for_new_project_from_twitter={
    "twitter_search_keyword":"merlin claim",
    "agents": {
        "new_project_analyzer":"new_project_analyzer_agent",
    },
    "tasks": [
        {
            "name": "new_project_analysis_twitter_task",
            "agent": "new_project_analyzer",
            "params": {
                "project_name": "merlin claim",
                "twitter_infos":"twitter_infos"
            }
        }
    ]
}

config_analysis_proxy_upgrade = {
    "event_loader_params": {
        "limit": 10,
        "type": "Proxy Upgrade",
        "severity": ["HIGH", "MEDIUM"]
    },
    "agents": {
        "brief":"brief_agent",
        "proxy_upgrade_analysis":"proxy_upgrade_analyzer_agent"
    },
    "tasks": [
        {
            "name": "brief_the_event_task",
            "agent": "brief",
            "params": {
                "events": "events"
            }
        },
        {
            "name": "proxy_upgrade_analysis_task",
            "agent": "proxy_upgrade_analysis",
            "params": {
            }
        }
    ]
}
config_analysis_price_slippage = {
    "event_loader_params": {
        "limit": 10,
        "type": "Price Slippage",
        # "trigger":"PriceSlippageETH",
        "severity": ["HIGH", "MEDIUM"],
        "query_string":{
            "tokenSymbol_value":"SPAI"
        }
    },
    "agents": {
        "brief":"brief_agent",
        "price_slippage_analysis":"price_slippage_analyzer_agent"
    },
    "tasks": [
        {
            "name": "brief_the_event_task",
            "agent": "brief",
            "params": {
                "events": "events"
            }
        },
        {
            "name": "price_slippage_analysis_task",
            "agent": "price_slippage_analysis",
            "params": {
            }
        }
    ]
}

config_analysis_erc20_mint_or_burn = {
    "event_loader_params": {
        "limit": 10,
        "type": "ERC20 Mint or Burn",
        "severity": ["HIGH", "MEDIUM"]
    },
    "agents": {
        "brief":"brief_agent",
        "erc20_mint_or_burn_analysis":"erc20_mint_or_burn_analyzer_agent"
    },
    "tasks": [
        {
            "name": "brief_the_event_task",
            "agent": "brief",
            "params": {
                "events": "events"
            }
        },
        {
            "name": "erc20_mint_or_burn_analysis_task",
            "agent": "erc20_mint_or_burn_analysis",
            "params": {
            }
        }
    ]
}
config_decompose_input_text_to_params_and_brief = {
    "event_loader_params": {
    },
    "agents": {
        "brief":"brief_agent",
        "decompose_input_text_to_params":"decompose_input_text_to_params_agent",
        "event_loader":"event_loader_agent"
    },
    "tasks": [
        {
            "name": "decompose_input_text_to_params_task",
            "agent": "decompose_input_text_to_params",
            "params": {
                "input_text": ""
            }
        },
        {
            "name": "event_loader_task",
            "agent": "event_loader",
            "params": {
            }
        },
        {
            "name": "brief_task",
            "agent": "brief",
            "params": {
            }
        }
    ]
}
