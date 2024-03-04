from datetime import datetime, timezone
from textwrap import dedent

from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun,DuckDuckGoSearchResults
# from tools import TokenTools
from tools import Web3EventLoader
from custom_tool import TwitterTool,EventTool
from langchain.agents import Tool
class Web3Agents():
	def __init__(self):
		# self.tokenTools = TokenTools()
		pass

	def security_analyse_agent(self):
		return Agent(
			role="安全分析师", 
			goal = '分析安全事件等级',
			backstory = dedent("""\
				作为非常资深并且见过大场面的web3 安全分析师, 对提供的事件进行安全鉴别和安全评级, 评级主要基于事件的安全影响, 分析完请给出 1. 事件分类 2. 事件评级 3. 事件概括. 评级包括 high, middium, low, informational."""),
			tools=[
				# DuckDuckGoSearchRun(),
				# TokenTools.fetch_token_technical_indicate
			],
			verbose=True,
			allow_delegation=False
		)
	def basic_analyzer_for_token_removal_agent(self):
		return Agent(
			role="uniswap专家", 
			goal = '分析流动性移除事件',
			backstory = dedent("""\
				作为一个非常优秀的uniswap专家, 你可以针对流动性移除事件进行分析, 并且用中文输出. 请给出你的分析结果, 以及你的分析过程.
			"""),
			tools=[
			],
			verbose=True,
			allow_delegation=False
		)
	def basic_writer_for_twitter_agent(self):
		return Agent(
			role="推文撰写员", 
			goal = '负责推文的撰写',
			backstory = dedent("""\
				作为一个非常优秀的推文撰写员, 你可以根据区块链专家的总结信息来发布推特，用中文输出推特内容.
			"""),
			tools=[
			],
			verbose=True,
			allow_delegation=False
		)
	def social_media_agent(self):
		return Agent(
			role='社交媒体运营专员',
			goal='负责推文的发布管理',
			backstory=dedent("""\
作为一个非常优秀的社交媒体运营专员, 负责根据监控到的安全事件来判断是否需要发布推文, 并且控制发布频率, 每天4~12 条. 如果确定需要发布, 则给出具体推文内容, 如果不需要发布, 则给出理由. """),
			verbose=True,
			allow_delegation=False
		)
	def liquidity_analysis_agent(self):
		return Agent(
			role="流动性事件分析师",
			goal="分析大额流动性移除事件",
			backstory=dedent("""\
				作为一个专注于流动性事件的分析师，你的任务是深入分析大额流动性移除事件，评估其对市场的可能影响。你需要基于事件的具体数据，如移除的金额、影响的代币以及相关交易地址，提供详尽的分析报告。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)

	def whale_movement_analysis_agent(self):
		return Agent(
			role="大额转账监测专家",
			goal="分析大额资金转移活动",
			backstory=dedent("""\
				身为一名大额转账监测专家，你需要关注和分析大额资金的转移活动，特别是那些可能对市场产生重大影响的“鲸鱼”行为。分析应包括转账的金额、参与的主要代币、来源和目的地址，以及这些活动可能表明的市场趋势。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def market_trend_analysis_agent(self):
		return Agent(
			role="市场趋势分析师",
			goal="预测市场对流动性事件的反应",
			backstory=dedent("""\
				作为市场趋势分析师，你负责预测特定事件，如大额流动性移除，对市场的潜在影响。你将分析市场历史数据、事件细节和可能的市场心理反应，以预测短期和长期的市场走向。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)

	def social_media_manager_agent(self):
		return Agent(
			role="社交媒体经理",
			goal="在社交媒体上发布分析和预测",
			backstory=dedent("""\
				作为社交媒体经理，你的任务是将分析结果和市场预测以吸引人的方式发布到社交媒体上，以增加用户参与度和品牌影响力。同时，监测和收集用户对发布内容的反馈。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)

	def user_feedback_collector_agent(self):
		return Agent(
			role="用户反馈收集员",
			goal="收集和分析社交媒体上的用户反馈",
			backstory=dedent("""\
				作为用户反馈收集员，你需要监控社交媒体上用户对我们发布的市场分析和预测的反应。收集用户评论、点赞、分享等互动数据，并进行初步分析，以评估我们的市场预测的接受度和准确性。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def brief_agent(self):
		return Agent(
			role="事件简报员",
			goal="整理最近的事件",
			backstory=dedent("""\
				作为事件整理员，你需要将最近发生的事件进行详细整理，并用中文输出。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def market_action_analysis_agent(self):
		return Agent(
			role="市场行为分析师",
			goal="分析市场行为风险",
			backstory=dedent("""\
				作为市场行为分析师，你需要分析事件中存在的潜在市场行为风险，并向我解释。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def new_project_analyzer_agent(self):
		return Agent(
			role="新项目分析员",
			goal="分析新项目",
			backstory=dedent("""\
				作为新项目分析员，你需要分析新项目的投资信息，可能的质押获利信息。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def new_project_agent(self):
		return Agent(
			role="新项目分析员",
			goal="分析新项目，决定下一步行动",
			backstory=dedent("""\
				作为新项目分析员，你要从搜索的结果整理中找到分析这个项目下一个要进行搜索的关键词。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def proxy_upgrade_analyzer_agent(self):
		return Agent(
			role="代理升级分析员",
			goal="分析代理升级",
			backstory=dedent("""\
				作为代理升级分析员，你需要分析代理升级的信息，可能的影响。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def price_slippage_analyzer_agent(self):
		return Agent(
			role="价格滑点分析员",
			goal="分析价格滑点",
			backstory=dedent("""\
				作为价格滑点分析员，你需要分析价格滑点的信息，可能的影响。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def erc20_mint_or_burn_analyzer_agent(self):
		return Agent(
			role="ERC20铸造销毁分析员",
			goal="分析ERC20铸造销毁",
			backstory=dedent("""\
				作为ERC20铸造销毁分析员，你需要分析ERC20铸造销毁的信息，可能的影响。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def price_manipulation_analyzer_agent(self):
		return Agent(
			role="价格操纵分析员",
			goal="分析价格操纵",
			backstory=dedent("""\
				作为价格操纵分析员，你需要分析价格操纵的信息，可能的影响。"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)
	def twitter_searcher_agent(self):
		twitter_search_tool=Tool(
			name="TwitterSearcher",
			func=TwitterTool._run,
			description="This tool is used to get the latest information about a project from Twitter.",
		)
		# tool的用法：在agent中定义然后放入tools中
		# tools=[twitter_search_tool]
		# 使用的时候，第一步的tools的参数会由task的params决定
		# 之后的所有搜索参数都会基于上一个的结果，如果上一步有结果的话
		# 如果tasks中的params定义了多个参数
		# 搜索的action input会是一个多个参数结果拼接而成的input
		return Agent(
			role="推特过滤员",
			goal="过滤推特信息",
			backstory=dedent("""\
				作为推特搜索员，你需要搜索推特信息。并从中总结出有关于区块链项目的信息"""),
			tools=[twitter_search_tool],
			verbose=True,
			allow_delegation=False
		)
	def event_loader_agent(self):
		event_loader_tool=Tool(
			name="EventLoader",
			func=EventTool._run,
			description="This tool is used to get the latest events from a project.",
		)
		return Agent(
			role="事件加载员",
			goal="加载事件",
			backstory=dedent("""\
				作为事件加载员，你需要根据输入的参数加载事件，如果你要整理，务必包含尽可能详细的信息。"""),
			tools=[event_loader_tool],
			verbose=True,
			allow_delegation=False
		)
	def decompose_input_text_to_params_agent(self):
		# 获取当前日期和时间（设置为UTC时区）
		current_datetime_utc = datetime.now(timezone.utc)

		# 格式化为ISO 8601格式的字符串
		iso_format_string = current_datetime_utc.isoformat()
		return Agent(
			role="输入解析员",
			goal="解析自然语言输入为查询的参数",
			backstory=dedent("""\
				作为输入解析员，你的任务是将自然语言输入解析为查询的参数
				不同场景的查询参数如下:
				监控场景内容	字段名	解释
				价格滑点	timestamp	时间戳
				价格滑点	type	类型
				价格滑点	network_value	网络值
				价格滑点	trigger	触发器
				价格滑点	severity	严重程度
				价格滑点	data_timestamp_value	数据时间戳值
				价格滑点	data_timestamp_displayValue	数据时间戳显示值
				价格滑点	tokenSymbol_value	代币符号值
				价格滑点	tokenAddress_href	代币地址链接
				价格滑点	tokenAddress_value	代币地址值
				价格滑点	liquidityPair_href	流动性对链接
				价格滑点	liquidityPair_value	流动性对值
				价格滑点	liquidityValue_unit	流动性值单位
				价格滑点	liquidityValue_value	流动性值
				价格滑点	slippagePercentage_value	滑点百分比值
				价格滑点	transactions	交易列表
				巨鲸	id	监控数据ID
				巨鲸	timestamp	时间戳
				巨鲸	url	URL
				巨鲸	plan	计划
				巨鲸	type	类型
				巨鲸	network_value	网络值
				巨鲸	trigger	触发器
				巨鲸	severity	严重程度
				巨鲸	data_timestamp_value	数据时间戳值
				巨鲸	data_timestamp_displayValue	数据时间戳显示值
				巨鲸	whaleName_value	鲸鱼名称
				巨鲸	whaleAddress_href	鲸鱼地址链接
				巨鲸	whaleAddress_value	鲸鱼地址值
				巨鲸	tokenSymbol_value	代币符号
				巨鲸	tokenAddress_href	代币地址链接
				巨鲸	tokenAddress_value	代币地址值
				巨鲸	valueInUsd_unit	价值单位
				巨鲸	valueInUsd_value	价值值
				巨鲸	tokenAmount_value	代币数量值
				巨鲸	transaction_href	交易链接
				巨鲸	transaction_value	交易值
				代理升级	timestamp	数据项生成的时间戳
				代理升级	type	数据类型
				代理升级	network_value	网络的数值
				代理升级	trigger	触发器
				代理升级	severity	严重程度
				代理升级	data_timestamp_value	数据时间戳的数值
				代理升级	data_timestamp_displayValue	数据时间戳的显示值
				代理升级	address_href	地址链接
				代理升级	address_value	地址值
				代理升级	newAddress_href	新地址链接
				代理升级	newAddress_value	新地址值
				代理升级	tokenSymbol_value	代币符号的数值
				大额流动性移除	timestamp	时间戳
				大额流动性移除	type	类型
				大额流动性移除	network_value	网络价值
				大额流动性移除	trigger	触发器
				大额流动性移除	severity	严重程度
				大额流动性移除	data_timestamp_value	数据时间戳值
				大额流动性移除	data_timestamp_displayValue	数据时间戳显示值
				大额流动性移除	transaction_href	交易链接
				大额流动性移除	transaction_value	交易值
				大额流动性移除	removalValue_unit	移除价值单位
				大额流动性移除	removalValue_value	移除价值
				大额流动性移除	senderAddress_href	发送者地址链接
				大额流动性移除	senderAddress_value	发送者地址值
				大额流动性移除	token0Address_href	代币0地址链接
				大额流动性移除	token0Address_value	代币0地址值
				大额流动性移除	token1Address_href	代币1地址链接
				大额流动性移除	token1Address_value	代币1地址值
				大额流动性移除	liquidityValue_unit	流动性价值单位
				大额流动性移除	liquidityValue_value	流动性价值
				大额流动性移除	liquidityAddress_href	流动性地址链接
				大额流动性移除	liquidityAddress_value	流动性地址值
				ERC20铸造或销毁	timestamp	数据时间戳
				ERC20铸造或销毁	type	数据类型
				ERC20铸造或销毁	network_value	网络值
				ERC20铸造或销毁	trigger	触发器
				ERC20铸造或销毁	severity	严重程度
				ERC20铸造或销毁	data_timestamp_value	数据时间戳值
				ERC20铸造或销毁	data_timestamp_displayValue	数据时间戳显示值
				ERC20铸造或销毁	valueInUsd_unit	价值单位
				ERC20铸造或销毁	valueInUsd_value	价值值
				ERC20铸造或销毁	tokenAmount_value	代币数量值
				ERC20铸造或销毁	tokenSymbol_value	代币符号值
				ERC20铸造或销毁	tokenAddress_href	代币地址链接
				ERC20铸造或销毁	tokenAddress_value	代币地址值
				ERC20铸造或销毁	transactions	相关交易列表
				network_value可选项有：bsc，eth，小写的
				可选的type返回结果只有5种：Price Slippage, Whale Movement, Proxy Upgrade, Large Liquidity Removal, ERC20 Mint or Burn
				查询时所需要的参数输入样例如下,这也是你需要输出的参数样例，是一个json数据，以{开始，}结束:
				另外注意，今天当下的时间是"""
				+iso_format_string+	
				"""
					{
				        "limit": xxx,(如果用户未指定，则默认为20）,)
						"time_start"（查询的开始时间范围，根据用户要求进行解析）: ISO 8601标准格式,
						"time_end"（查询的结束时间范围，根据用户要求进行解析）: ISO 8601标准格式, 
						"type": "xxxx"(可选的type返回结果只有5种：Price Slippage, Whale Movement, Proxy Upgrade, Large Liquidity Removal, ERC20 Mint or Burn),
						"query_string":{
								"xxxxx":"xxxxx"
						}
					}
				以上参数中，任何带有下划线的数据查询解析都应该放在query_string中
				
				另外，如果查询的是与攻击事件相关的，则忽略以上设定，返回共计相关的参数样例，是一个json数据，以{开始，}结束:
				id	唯一标识符，用于识别每个特定的事件或记录。
				createdAt	记录创建时间。
				updatedAt	记录最后更新时间。
				title	事件或记录的标题。
				attackTime	攻击发生时间。
				meta	元数据，包含了一些额外信息，此字段为空。
				chainSlug	事件发生的区块链简称，例如 'eth' 代表以太坊。'bsc'代表币安链bnb chain
				mwe	未说明，但通常用于表示最小工作示例或最小工作环境。可能是None表示此字段未被使用。
				description	事件的描述。
				poc	概念验证，用于证明安全漏洞或攻击手段的可行性。
				totalLossUsd	总损失额（美元）
				lossUsd	实际损失额（美元）
				lossTokenSymbol	损失的代币符号，此字段为空。
				lossTokenAmount	损失的代币数量，
				transactions	与事件相关的交易ID列表。
				messageIds	消息ID列表，此字段为空。
				projectId	项目ID，用于关联事件所属的特定项目或组织。
				state	事件状态，'CONFIRMED' 表示已确认。
				confirmedAt	事件确认时间，此字段为空。
				confirmedBy	确认事件的人或实体，此字段为空。
				archived	表示记录是否已归档，False 表示未归档。
				archivedAt	记录归档时间，此字段为空。
					{
						"limit": xxx（如果用户未指定，则默认为20）,
						"time_start"（查询的开始时间范围，根据用户要求进行解析，如果无要求则为最近2天）: ISO 8601标准格式,
						"time_end"（查询的结束时间范围，根据用户要求进行解析，如果无要求则为今天）: ISO 8601标准格式, 

						"type": "attack"(此字段不变，固定为attack),
						"query_string":{
							"xxxxx":"xxxxx"
						}

					"""),
			tools=[],
			verbose=True,
			allow_delegation=False
		)

	