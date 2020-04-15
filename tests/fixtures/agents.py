# strategy maps a set of historical states to future actions
# a behavior chooses a strategy that maximizes the utility of that behavior
# should take generics CoolAgent(BaseAgent[Strategy,bitarray,])
from typing import NamedTuple, TypeVar

from mesa_behaviors.agents.base_agent import BaseAgent
from mesa_behaviors.utility.base_utility import BaseUtility
from mesa_behaviors.utility.binary import BinaryUtilityScore


S = TypeVar("S")
H = TypeVar("H")


class DummyAgentFeatures(NamedTuple):
    happy: int


class DummyAgent(BaseAgent[S, H, DummyAgentFeatures]):
    def __init__(
        self,
        strategies: S,
        utility: BaseUtility[S, H, BinaryUtilityScore],
        historical_func: H,
        label: str,
    ):
        super().__init__(strategies, utility, historical_func, label)
        self.latest_scores: BinaryUtilityScore = {}
        self.feature = DummyAgentFeatures(happy=0)

    def features(self) -> DummyAgentFeatures:
        return self.feature

    def select(self, scores: BinaryUtilityScore):
        score = sorted(scores.items(), key=lambda x: x[1]["score"])[-1][1]
        return score["prediction"]

    def step(self):

        self.latest_scores = self.utility.utility_score(self.strategies, self.history)
        action = self.select(self.latest_scores)
        if action == 1:
            self.feature = DummyAgentFeatures(happy=1)
        else:
            self.feature = DummyAgentFeatures(happy=0)

    def label(self):
        self.label_name


class MiniAgent(BaseAgent[S, H, int]):
    def __init__(
        self,
        strategies: S,
        utility: BaseUtility[S, H, int],
        historical_func: H,
        label: str,
    ):
        super().__init__(strategies, utility, historical_func, label)
        self.latest_scores: int = 0
        self.feature = 0

    def features(self) -> int:
        return self.feature

    def select(self, scores: int):
        return scores

    def label(self):
        self.label_name

    def step(self):
        self.latest_scores = self.utility.utility_score(self.strategies, self.history)
        self.select(self.latest_scores)
        self.feature = self.feature + 1
