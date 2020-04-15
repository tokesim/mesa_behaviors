from typing import Dict, NamedTuple


# dictates per sequence of results which action to take
StrategyMap = Dict[int, int]


class Strategy(NamedTuple):
    action_seq_map: StrategyMap
    uuid: str


# uuid str to strategy
Strategies = Dict[str, Strategy]
