from math import log, ceil
from typing import Optional, List, NewType, Tuple, Dict
from util import *

"""

n * log_n       iterations
log_n           new windows need to be compared per iteration
n               comparisons for each window
log_n           operations for each comparison

TOTAL: n^2 * (log_n)^3

"""


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
