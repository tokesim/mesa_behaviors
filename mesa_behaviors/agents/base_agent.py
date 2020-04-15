from abc import ABC, abstractclassmethod, abstractmethod
from typing import Any, Generic, TypeVar

from mesa import Agent

from mesa_behaviors.utility.base_utility import BaseUtility


# strategy shape
S = TypeVar("S")
# historical function shape
H = TypeVar("H")
# features
F = TypeVar("F")


class BaseAgent(Agent, Generic[S, H, F], ABC):
    """
    This is the base class for all Agents, it takes generics to specify
    unified features, historical functionality, and individual agent strategies

    :param strategies: A set of encoded strategies an agent might employ:
    :param utility: A utility class that takes an arbitrary strategy and
    history set
    :param historical_func: A function to retrieve the model historical state from
    :param label: A label for the Agent

    """

    def __init__(
        self,
        strategies: S,
        utility: BaseUtility[S, H, Any],
        historical_func: H,
        label: str,
    ):
        super().__init__(None, None)
        self.utility = utility
        self.strategies = strategies
        self.history = historical_func
        self.label_name = label

    @staticmethod
    @abstractclassmethod
    def label() -> str:
        pass

    @abstractmethod
    def features(self) -> F:
        pass

    def set_id(self, id: Any) -> Any:
        self.unique_id = id
        return self

    def set_historical_func(self, historical_func: H) -> Any:
        self.history = historical_func
        return self

    def set_model(self, model: Any) -> Any:
        self.model = model
        return self
