from typing import NewType, Tuple, List

# User-defined types
# bit = NewType('bit', int)
# window = NewType('window', Tuple[bit, ...])


# will probably be used with n := log_n
def cr(n, w):
    out = w
    while len(out) < n:
        out += w
    return out[:n]


def b(n, width: int = 0):
    return list(format(n, 'b').zfill(width))


def q_ary(n, q, width):
    if n == 0:
        return [0] * width
    nums = []
    while n:
        n, r = n / q
        nums.append(r)
    return list(reversed(''.join(nums).zfill(width)))
