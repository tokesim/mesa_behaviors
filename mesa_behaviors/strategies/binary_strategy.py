import math
import random
from typing import Dict, NamedTuple
from uuid import UUID, uuid4


# dictates per sequence of results which action to take
# should be constrained to 0 or 1
BinaryDigit = int
BinaryStrategyMap = Dict[int, BinaryDigit]


class BinaryStrategy(NamedTuple):
    binary_seq_map: BinaryStrategyMap
    window_size: int
    uuid: UUID


# uuid str to strategy
BinaryStrategies = Dict[str, BinaryStrategy]


def generate_random_strategy(m: int, uuid: UUID) -> BinaryStrategy:
    possible_sequences = int(math.pow(m, 2))
    return BinaryStrategy(
        binary_seq_map={s: random.choice([0, 1]) for s in range(possible_sequences)},
        uuid=uuid,
        window_size=m,
    )


def generate_binary_strategies(num_strategies: int, m: int) -> BinaryStrategies:
    strategies: BinaryStrategies = {}
    for x in range(num_strategies):
        uuid = uuid4()
        strategies[str(uuid)] = generate_random_strategy(m, uuid)
    return strategies
