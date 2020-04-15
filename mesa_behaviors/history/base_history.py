from abc import ABC, abstractmethod
from typing import Generic, TypeVar


H = TypeVar("H")
T = TypeVar("T")


class BaseHistory(Generic[H, T], ABC):
    @abstractmethod
    def add(self, entry: T) -> None:
        pass

    @abstractmethod
    def retrieve(self) -> H:
        pass
