from abc import ABC
from typing import Callable, Dict

from bitarray import bitarray
import bitarray.util as bitarray_util
from mypy_extensions import TypedDict

from mesa_behaviors.strategies.binary_strategy import BinaryStrategies
from mesa_behaviors.utility.base_utility import BaseUtility


BinaryHistoryFunc = Callable[[], bitarray]


def get_window_size(strategies: BinaryStrategies) -> int:
    key = next(iter(strategies))
    return strategies[key].window_size


class Score(TypedDict):
    prediction: int
    score: int


BinaryUtilityScore = Dict[str, Score]


def flat_score(
    strategies: BinaryStrategies,
    history_func: BinaryHistoryFunc,
    score: Callable[[int, int], int],
) -> BinaryUtilityScore:
    window_size = get_window_size(strategies)
    history = history_func()
    scores = {uuid: Score({"score": 0, "prediction": -1}) for uuid in strategies.keys()}
    for i in range(len(history)):
        if i + window_size >= len(history):
            return scores

        encoded_seq = bitarray_util.ba2int(history[i : window_size + i])
        next_state = history[window_size + i]

        for uuid, strategy in strategies.items():
            prediction = strategy.binary_seq_map[encoded_seq]
            scores[uuid]["prediction"] = prediction
            scores[uuid]["score"] = scores[uuid]["score"] + score(
                prediction, next_state
            )
    return scores


class Utility(BaseUtility[BinaryStrategies, bitarray, BinaryUtilityScore], ABC):
    def __init__(self) -> None:
        pass


class BinaryMinorityUtility(Utility):
    def score(self, prediction: int, next_state: int) -> int:
        if prediction == next_state:
            return -1
        else:
            return 1

    def utility_score(
        self, strategies: BinaryStrategies, history: BinaryHistoryFunc
    ) -> BinaryUtilityScore:
        return flat_score(strategies, history, self.score)


class BinaryMajorityUtility(Utility):
    def score(self, prediction: int, next_state: int) -> int:
        if prediction == next_state:
            return 1
        else:
            return -1

    def utility_score(
        self, strategies: BinaryStrategies, history: BinaryHistoryFunc
    ) -> BinaryUtilityScore:
        return flat_score(strategies, history, self.score)
