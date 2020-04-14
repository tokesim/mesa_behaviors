from typing import TypeVar, Generic, Callable
from abc import abstractmethod, ABC


T = TypeVar("T")
S = TypeVar("S")
H = TypeVar("H")


class BaseUtility(Generic[S, H, T], ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def utility_score(self, strategies: S, history: Callable[[], H]) -> T:
        pass
