from typing import List
from uuid import uuid4

from bitarray import bitarray

from mesa_behaviors.strategies.binary_strategy import BinaryStrategies, BinaryStrategy
from mesa_behaviors.utility import binary


def _create_binary_map(predictions: List[int]):
    return {idx: prediction for idx, prediction in enumerate(predictions)}


TEST_STRATEGY1 = [
    [0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 1],
]

TEST_STRATEGY2 = [
    [0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]


TEST_STRATEGY3 = [
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
]


def create_test_strategies(strategies, window_size) -> BinaryStrategies:
    binary_strategies: BinaryStrategies = {}
    for idx, strategy in enumerate(strategies):
        seq_map = {i: prediction for i, prediction in enumerate(strategy)}
        uuid = uuid4()
        binary_strategies[str(uuid)] = BinaryStrategy(
            binary_seq_map=seq_map, window_size=window_size, uuid=uuid
        )
    return binary_strategies


BIN_TEST_STRATEGIES_1 = create_test_strategies(TEST_STRATEGY1, 3)


def test_binary_flat_score():
    # not enough history to present a result resulting in a null predicted action
    scores = binary.flat_score(
        BIN_TEST_STRATEGIES_1,
        lambda: bitarray([0, 1, 1]),
        lambda x, y: 1 if x == y else -1,
    )
    print(scores)
    # encoded values for 3 result in prediction 1 resulting in score -1 compared with historical result
    scores = binary.flat_score(
        BIN_TEST_STRATEGIES_1,
        lambda: bitarray([0, 1, 1, 0]),
        lambda x, y: 1 if x == y else -1,
    )
    print(scores)
    # encoding of 6 with predictions [1 0 0 1] resulting in score -2 ,0, 0 -2
    scores = binary.flat_score(
        BIN_TEST_STRATEGIES_1,
        lambda: bitarray([0, 1, 1, 0, 1]),
        lambda x, y: 1 if x == y else -1,
    )
    print(scores)


def test_binary_minority_utility():
    util = binary.BinaryMinorityUtility()
    scores = util.utility_score(
        BIN_TEST_STRATEGIES_1, lambda: bitarray([0, 1, 1, 0, 1])
    )
    print(scores)


def test_binary_majority_utility():
    util = binary.BinaryMajorityUtility()
    scores = util.utility_score(
        BIN_TEST_STRATEGIES_1, lambda: bitarray([0, 1, 1, 0, 1])
    )
    print(scores)
