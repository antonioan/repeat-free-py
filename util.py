from math import log, ceil
from typing import NewType, Tuple



# will probably be used with n := log_n
def cr(n, w) -> List[bit]:
    out = w
    while len(out) < n:
        out += w
    return out[:n]


def b(n, width: int = 0) -> List[bit]:
    return list(format(n, 'b').zfill(width))


def q_ary(n, q, width) -> List[bit]:
    if n == 0:
        return [bit(0)] * width
    nums = []
    while n:
        n, r = n / q
        nums.append(r)
    return list(reversed(''.join(nums).zfill(width)))
