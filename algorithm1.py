from math import log, ceil
from typing import Optional, List, NewType, Tuple, Dict

# User-defined types
bit = NewType('bit', int)
window = NewType('window', Tuple[bit, ...])


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
        n, r = divmod(n, q)
        nums.append(r)
    return list(reversed(''.join(nums).zfill(width)))


class Algorithm1:
    # region Parameters
    # FIELD     TYPE                    SKETCH NAME     DOMAIN          RANGE           DESCRIPTION
    input:      List[bit]               # s             [n]             bit             .
    w:          List[bit]               # w             [len]           bit             .
    n:          int                     # n             -               -               .
    len:        int                     # n_tag         -               Max Ext. Index  .
    q:          int                     # q             -               -               .
    log_n:      int                     # log_n         -               -               .
    k:          int                     # k             -               -               .
    # endregion

    def __init__(self, s, q: int = 2):
        if not isinstance(s, list):
            raise Exception("Input must be a list.")
        if q != 2:
            raise NotImplementedError()
        self.input = s
        self.w = []
        self.n = len(s) + 1
        self.len = 0
        self.q = q
        self.log_n = ceil(log(self.n, self.q))
        self.k = 2 * self.log_n + 2

    def encode(self, _debug_no_append=False):
        w_list = self.input + [bit(1)] + ([bit(0)] * (self.log_n + 1)) if not _debug_no_append else self.input
        self.w = w_list
        self.len = len(self.w)

        # TODO: Initialize data structures

        # Run algorithm
        self.eliminate()
        self.expand()

    def eliminate(self):
        while True:
            raise NotImplementedError()

    def expand(self):
        while len(self.w) < self.n:
            # raise NotImplementedError()
            break
        self.w = self.w[:self.n]

    def output(self):
        return self.w
