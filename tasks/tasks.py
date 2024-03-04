from textwrap import dedent

from crewai import Task
from tools import Web3EventLoader

class Web3Tasks:
	def events_analyse_task(self, agent, posted, new_events):
		return Task(
			description=dedent(f"""\
You are an experienced security analyst. You will be provided with a list of security events. 
Your task is to analyze each of these events and determine three things: 
1) Classification of the event
2) Rating of the event - this could be high, medium, low, or informational, based on the security impact of the event
3) A brief summary of the event 
Your analysis should be thorough, providing the right category, rating, and short summary for each event in the list. 
Remember, your expertise is crucial here to ensure each event is appropriately evaluated and classified based on its severity and impact.

Posted: 
{posted}

New Events: 
{new_events}
"""),
			agent=agent
		)
	def liquidity_removal_explain_task(self,agent,posted,events):
		return Task(
			description=dedent(f"""\
					   帮我解读一下最近这段时间的liquidity remove情况 ，用中文输出
					   Posted:
					   {posted}
					   New Events:
					   {events}
					   """),
					   agent=agent
		)
	def twitter_writer_for_liquidity_removal_task(self, agent,posted,events):
		return Task(
			description=dedent(f"""\
					  根据分析结果来撰写有关流动性移除的推文，用中文输出
					  
					  """),
			agent=agent
		)
	def analyze_liquidity_removal_event_task(self, agent, events):
		return Task(
			description=dedent(f"""\
				分析并报告最近的大额流动性移除事件。请基于提供的事件数据，评估事件的影响并预测可能的市场反应。确保分析包括事件的规模、涉及的代币以及任何相关的市场动向。
				事件数据:
				{events}
				"""),
			agent=agent
		)
	def basic_twitter_send_task(self,agent):
		return Task(
			description=dedent(f"""\
				根据分析结果来撰写有关的推文，用中文输出
				"""),
			agent=agent
		)
	def analyze_whale_movement_event_task(self, agent, events):
		return Task(
			description=dedent(f"""\
				分析并报告最近的大额资金转移活动。关注特定的“鲸鱼”行为，包括资金的来源和去向，以及这些活动对市场可能产生的影响。评估是否存在市场操纵或其他重要的市场动态。
				事件数据:
				{events}
				"""),
			agent=agent
		)
	def predict_market_response_task(self, agent):
		return Task(
			description=dedent(f"""\
				基于流动性移除事件的分析，预测市场的可能反应。考虑事件的规模、涉及的资产和历史市场反应模式，预测短期内市场的波动情况及长期趋势。
				
				"""),
			agent=agent
		)
	def hidden_action_analysis_task(self, agent):
		return Task(
			description=dedent(f"""\
				这些数据中存在一个潜在的与市场行为风险，把它找出来，并向我详细的解释风险行为，以及后续可能发生的事情
				，必须是实际的而非模棱两可的回答，且必须包含地址，数量等解析，同时，尽量包含交易链接
				"""),
			agent=agent
		)
	def brief_the_event_task(self,agent,events):
		return Task(
			description=dedent(f"""\
				将最近的发生的事件进行简要整理，用中文输出，尽量包含交易链接
				你的分析应该尽可能详细，不应丢掉任何信息，不论其是否重要
				{events}
				"""),
			agent=agent
		)
	def brief_task(self,agent):
		return Task(
			description=dedent(f"""\
				将最近的发生的事件进行简要整理，用中文输出，尽量包含交易链接
				你的分析应该尽可能详细，不应丢掉任何信息，不论其是否重要
				"""),
			agent=agent
		)
	def publish_analysis_and_prediction_task(self, agent, market_prediction):
		return Task(
			description=dedent(f"""\
				将市场预测和事件分析结果制作成吸引人的内容，并发布到社交媒体上。内容应包括关键分析要点、市场预测、图表或视觉元素，以及鼓励用户反馈的呼吁。
				市场预测:
				{market_prediction}
				"""),
			agent=agent
		)

	def collect_user_feedback_task(self, agent, social_media_posts):
		return Task(
			description=dedent(f"""\
				监控社交媒体上对我们发布内容的用户反馈。收集用户评论、点赞、分享等数据，并进行分析，以评估市场对我们分析和预测的接受程度和反应。
				社交媒体帖子:
				{social_media_posts}
				"""),
			agent=agent
		)
	def new_project_analysis_task(self,agent,project_name):
		return Task(
			description=dedent(f"""\
				分析新项目{project_name}是否能够成为下一个热门项目，它的投资价值如何，最近有什么新的质押活动或者动态
				"""),
			agent=agent
		)
	def new_project_analysis_twitter_task(self,agent,project_name,twitter_infos):
		return Task(
			description=dedent(f"""\
				分析新项目{project_name}最近有什么新的质押活动或者动态，并且把相应的质押或者投资的链接以及推特的链接给我
				以下是推特动态信息{twitter_infos}
				"""),
			agent=agent
		)
	def new_project_analysis_twitter_get_next_keyword(self,agent,project_name,twitter_infos):
		return Task(
			description=dedent(f"""\
				分析新项目{project_name}最近有什么新的质押活动或者动态，并且提取一个下一步要进行搜索的关键词
				以下是推特动态信息{twitter_infos}
				"""),
			agent=agent
		)
	def proxy_upgrade_analysis_task(self, agent, events):
		return Task(
			description=dedent(f"""\
				分析最近的代理升级事件。请基于提供的事件数据，评估事件的影响并预测可能的市场反应。确保分析包括事件的规模、涉及的代币以及任何相关的市场动向。
				事件数据:
				{events}
				"""),
			agent=agent
		)
	def price_slippage_analysis_task(self, agent):
		return Task(
			description=dedent(f"""\
				分析最近的价格滑点事件。请基于提供的事件数据，评估事件的影响并预测可能的市场反应。确保分析包括事件的规模、涉及的代币以及任何相关的市场动向。
				"""),
			agent=agent
		)
	def erc20_mint_or_burn_analysis_task(self, agent, events):
		return Task(
			description=dedent(f"""\
				分析最近的ERC20代币铸造或销毁事件。请基于提供的事件数据，评估事件的影响并预测可能的市场反应。确保分析包括事件的规模、涉及的代币以及任何相关的市场动向。
				你的分析步骤如下：
				1. 事件的规模
				2. 涉及的代币
				3. 事件的市场影响
				4. 事件的可能原因
				5. 预测市场的可能反应
				
				事件数据:
				{events}
				"""),
			agent=agent
		)
	def twitter_deep_search_keyword_task(self,agent,project_name):
		# twitter_res=Web3EventLoader._get_twitter_search(project_name)
		return Task(
			description=dedent(f"""\
				根据提供的推特搜索结果，总结下有关于{project_name}这个区块链项目的信息。
				抽取出要进行下一步深入搜索的关键词并输出，仅输出这个关键词即可
				注意结果应该是一个单词或者短语
				"""),
			agent=agent
		)
	def twitter_search_info_task(self,agent):
		return Task(
			description=dedent(f"""\
				根据上一步总结的关键词，进行推特搜索，根据提供的推特搜索结果，总结下有关于这个区块链项目的信息。
				"""),
			agent=agent
		)
	def price_manipulation_analysis_task(self, agent, events):
		return Task(
			description=dedent(f"""\
				分析最近的价格操纵事件。请基于提供的事件数据，评估事件的影响并预测可能的市场反应。确保分析包括事件的规模、涉及的代币以及任何相关的市场动向。
				此外，还需要分析事件的可能原因和潜在的市场操纵行为。
				最后，根据分析结果，预测市场的可能反应。
				你的分析内容如下：
				1. 事件的规模
				2. 涉及的代币
				3. 事件的市场影响
				4. 事件的可能原因
				5. 预测市场的可能反应
				事件数据:
				{events}
				"""),
			agent=agent
		)
	def decompose_input_text_to_params_task(self, agent, input_text):
		return Task(
			description=dedent(f"""\
				将输入的文本分解为参数。根据输入的文本，提取出其中的关键的用户要查询的信息，并输出。
				输入文本:
				{input_text}
				输出格式：
				"""),
			agent=agent
		)
	def event_loader_task(self,agent):
		return Task(
			description=dedent(f"""\
				根据输入的参数使用tool加载事件。并务必包含详细信息，不要进行总结"""),
			agent=agent
		)
	def social_media_check_task(self, agent, posted, events):
		return Task(
			description=dedent(f"""\
As an AI, you will be given a list of recent events and the tweets you have posted in the last 24 hours. 
First, you need to check if any of the events in the list are repetitive or similar to the content you have already tweeted. 
Then, based on their importance, identify the most significant events. Finally, compile a list of events that should be tweeted. 
Remember, your goal is to avoid redundancy and prioritize the most important and relevant events.

Your final answer MUST be with:
- if to post : yes or no 
- reasoning
- [optional] twitter body: if need to pos 
					  
Posted: 
{posted}

New Events: 
{events}"""),
			agent=agent
		)
