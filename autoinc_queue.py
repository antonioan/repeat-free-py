from collections import deque
from typing import Iterable, Optional


class AutoIncQueue(deque):
    def __init__(self, iterable: Optional[Iterable[int]] = None,
                 maxlen: Optional[int] = None,
                 autoincrement: bool = False,
                 increment_until: Optional[int] = None):
        if iterable is None:
            iterable = ()
        deque.__init__(self, iterable=iterable, maxlen=maxlen)
        self._autoincrement = autoincrement
        self._increment_until = increment_until if autoincrement else None

    @property
    def autoincrement(self):
        return self._autoincrement

    @autoincrement.setter
    def autoincrement(self, flag: bool):
        self._autoincrement = flag

    @property
    def increment_until(self):
        return self._increment_until

    @increment_until.setter
    def increment_until(self, val: int):
        self._increment_until = val

    def pop(self, i: int = ...) -> int:
        if len(self) == 1 and (i is None or i == 0) and self._increment_until and self[-1] < self._increment_until:
            self.appendleft(self[-1] + 1)
        return deque.pop(self, i)

    def popleft(self) -> int:
        if len(self) == 1 and self._increment_until and self[0] < self._increment_until:
            self.append(self[0] + 1)
        return deque.popleft(self)

    def remove(self, value: int) -> None:
        if len(self) == 1 and value == self[0] and self._increment_until and self[0] < self._increment_until:
            self.append(self[0] + 1)
        return deque.remove(self, value)
