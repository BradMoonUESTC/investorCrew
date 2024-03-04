from agents.agents import Web3Agents
from crewai import Crew
from tasks.tasks import Web3Tasks


class Web3SecurityCrew():
	def __init__(self, config):
		self.config = config
		self.agents = Web3Agents()
		self.tasks = Web3Tasks()

	def get_agent_instance(self, agent_name):
		return getattr(self.agents, agent_name)()

	def kickoff(self, state):
		crew_agents = []
		crew_tasks = []

		for agent_key, agent_name in self.config['agents'].items():
			setattr(self, agent_key, self.get_agent_instance(agent_name))

		for task_info in self.config['tasks']:
			task_name = task_info['name']
			agent_instance = getattr(self, task_info['agent'])
			
			task_params = {k: state[v] if v in state else v for k, v in task_info['params'].items()}
			task_method = getattr(self.tasks, task_name)
			crew_tasks.append(task_method(agent_instance, **task_params))

		crew = Crew(agents=crew_agents, tasks=crew_tasks, verbose=True)
		
		result = crew.kickoff()
		return {**state, "result": result}
