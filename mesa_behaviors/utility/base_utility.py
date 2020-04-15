from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar


T = TypeVar("T")
S = TypeVar("S")
H = TypeVar("H")


class BaseUtility(Generic[S, H, T], ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def utility_score(self, strategies: S, history: Callable[[], H]) -> T:
        pass
