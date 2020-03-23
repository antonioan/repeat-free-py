from typing import NewType, Tuple, List, Optional


# will probably be used with n := log_n
def cr(n, w):
    out = w
    while len(out) < n:
        out += w
    return out[:n]


def b(n, width: int = 0):
    return list(format(n, 'b').zfill(width))


# Time complexity: O(log(n, base=q))
# Place complexity: O(log_q) * O(log(n, base=q))
def q_ary(n, q, width):
    if n == 0:
        return [0] * width
    nums = []
    while n:
        n, r = n / q
        nums.append(r)
    return list(reversed(''.join(nums).zfill(width)))
