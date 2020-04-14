from typing import Callable, Sequence

from mesa_behaviors.utility.base_utility import BaseUtility


class DummyUtility(BaseUtility[int, Sequence[int], int]):
    def utility_score(self, strategies: int, history: Callable[[], Sequence[int]]):
        return 99


class DummyUtility1(BaseUtility[int, Sequence[int], int]):
    def utility_score(self, strategies: int, history: Callable[[], Sequence[int]]):
        return 101
