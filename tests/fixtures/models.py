from mesa.datacollection import DataCollector
from mesa.time import BaseScheduler

from mesa_behaviors.agents.population import AgentPopulation
from mesa_behaviors.history.binary import BinaryHistory
from mesa_behaviors.models.base_model import BaseModel
from tests.fixtures.agents import DummyAgentFeatures


# There exists some function that you can Type to reference the required returned state of an agent So an AgentPopulation
# is typed to return a subset of state that you can reference in the model to build aggregate statistics
# The aim is to be abble to call binary_encode_state in a typesafe way or a type constrained way because you know the agent
# population is bound to contain a subset of data


class DummyModel(BaseModel):
    def __init__(
        self,
        agent_population: AgentPopulation[DummyAgentFeatures],
        schedule: BaseScheduler,
        history: BinaryHistory,
        terminal_step: int,
    ):
        super().__init__(agent_population, schedule(self), history)
        self.datacollector = DataCollector(
            {},
            {
                "happy": lambda agent: agent.features().happy
            },  # Model-level count of happy agents
        )
        self.running = True
        self.terminal_step = terminal_step

    def encode_history(self):
        happiness = sum([agent.features().happy for agent in self.agents]) / len(
            self.agents
        )
        if happiness > 0.5:
            return 1
        else:
            return 0

    def step(self):
        majority_happy = self.encode_history()
        self.history.add(majority_happy)
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)
        if self.schedule.steps >= self.terminal_step:
            self.running = False
