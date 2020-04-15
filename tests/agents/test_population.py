import random

from mesa_behaviors.agents.population import (
    AgentLabels,
    AgentTypeMap,
    generate_population,
)
from tests.fixtures import strategy
from tests.fixtures.agents import DummyAgent
from tests.fixtures.utility import DummyUtility, DummyUtility1


def dummy_distribution(agent_labels: AgentLabels, size: int) -> AgentLabels:
    return random.choices(agent_labels, k=size)


def get_dummy_history():
    return [0, 1, -1, 0, 1]


def test_generating_population():
    typesMap: AgentTypeMap = {
        "greedy": lambda: DummyAgent(
            strategy.generate_trinary_strategies(4, 3),
            DummyUtility(),
            get_dummy_history,
            "greedy",
        ),
        "avg": lambda: DummyAgent(
            strategy.generate_trinary_strategies(4, 3),
            DummyUtility1(),
            get_dummy_history,
            "avg",
        ),
    }
    generator = generate_population(dummy_distribution, typesMap, 10)
    agents1 = generator()
    agents2 = generator()
    assert len(agents1) == 10
    assert len(agents2) == 10
    # TODO assert that the distrubtion is correct it's unlikely for a perfect match but could happen
    assert [agent.label for agent in agents1] != [agent.label for agent in agents2]
