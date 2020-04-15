from tests.fixtures.agents import MiniAgent
from tests.fixtures.utility import DummyUtility


def test_constructing_agent():
    MiniAgent(100, DummyUtility(), lambda: [1, 0, 1, 0, -1], "newagent")


def test_agent_step():
    agent = MiniAgent(100, DummyUtility(), lambda: [1, 0, 1, -1], "newagent")
    agent.step()
    assert agent.latest_scores == 99
