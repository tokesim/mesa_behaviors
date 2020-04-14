from abc import ABC

from mesa import Model
from mesa.time import BaseScheduler

from mesa_behaviors.agents.population import AgentPopulation
from mesa_behaviors.history.base_history import BaseHistory


class BaseModel(Model, ABC):
    def __init__(
        self,
        agent_population: AgentPopulation,
        schedule: BaseScheduler,
        history: BaseHistory,
    ):
        super().__init__()
        self.agents = agent_population
        self.schedule = schedule
        self.history = history
        [agent.set_id(idx).set_model(self) for idx, agent in enumerate(self.agents)]
        # schedule agents
        [self.schedule.add(agent) for agent in self.agents]
        self.running = True
