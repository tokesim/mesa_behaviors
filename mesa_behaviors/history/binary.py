from bitarray import bitarray

from mesa_behaviors.history.base_history import BaseHistory


class BinaryHistory(BaseHistory[bitarray, int]):
    def __init__(self, initial_history: bitarray = None):
        self.history = bitarray()
        if initial_history is not None:
            self.history = initial_history

    def add(self, entry: int) -> None:
        if entry == 0:
            self.history.append(0)
            return
        if entry == 1:
            self.history.append(1)
            return
        raise ValueError("Entry should be 1 or 0")

    def retrieve(self) -> bitarray:
        return self.history
