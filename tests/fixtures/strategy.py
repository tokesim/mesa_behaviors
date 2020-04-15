import math
import random
from typing import Dict, NamedTuple
from uuid import uuid4


# dictates per sequence of results which action to take
StrategyMap = Dict[int, int]


class Strategy(NamedTuple):
    action_seq_map: StrategyMap
    uuid: str


# uuid str to strategy
Strategies = Dict[str, Strategy]


def generate_random_strategy(m: int, uuid: str) -> Strategy:
    possible_sequences = int(math.pow(m, 2))
    return Strategy(
        action_seq_map={
            s: random.choice([-1, 0, 1]) for s in range(possible_sequences)
        },
        uuid=uuid,
    )


def generate_trinary_strategies(num_strategies: int, m: int) -> Strategies:
    strategies = {}
    for x in range(num_strategies):
        uuid = uuid4()
        strategies[str(uuid)] = generate_random_strategy(m, str(uuid))
    return strategies
