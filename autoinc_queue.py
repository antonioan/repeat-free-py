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
        self._prev = iterable[0] if iterable is not None else None

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

    @property
    def prev(self):
        return self._prev

    def pop(self, i: int = ...) -> int:
        if len(self) == 1 and (i is None or i == 0) and self._increment_until and self[-1] < self._increment_until:
            self.appendleft(self[-1] + 1)
        self._prev = self[-1]
        return deque.pop(self, i)

    def popleft(self) -> int:
        if len(self) == 1 and self._increment_until and self[0] < self._increment_until:
            self.append(self[0] + 1)
        self._prev = self[0]
        return deque.popleft(self)

    # Assumes value is found; otherwise, prev is wrong
    def remove(self, value: int) -> None:
        if len(self) == 1 and value == self[0] and self._increment_until and self[0] < self._increment_until:
            self.append(self[0] + 1)
        self._prev = value
        return deque.remove(self, value)

    # Supported base methods:

    def insert(self, i: int, x: int) -> None:
        deque.insert(self, i, x)

    def append(self, x: int) -> None:
        deque.append(self, x)

    def appendleft(self, x: int) -> None:
        deque.appendleft(self, x)

    def clear(self) -> None:
        deque.clear(self)

    def extend(self, iterable: Iterable[int]) -> None:
        deque.extend(self, iterable)

    def extendleft(self, iterable: Iterable[int]) -> None:
        deque.extendleft(self, iterable)

    def empty(self) -> bool:
        return len(self) == 0
