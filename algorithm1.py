from math import log, ceil
from utils import *

"""

n * log_n       iterations
n   OR?  log_n  new windows need to be compared per iteration
n               comparisons for each window
log_n           operations for each comparison

TOTAL: n^3 * (log_n)^2   OR?  n^2 * (log_n)^3

TIME                       SPACE
-----                      -----
  n^3 * (log_n)^2    |       1 (log_n for int representation)
  n^2 * (log_n)^2    |       n          (?)
  n^2 * log_n        |       n * log_n
  n   * (log_n)^2    |       n^2

"""


class Algorithm1:
    # region Parameters
    # FIELD     TYPE                    SKETCH NAME     DOMAIN          RANGE           DESCRIPTION
    w:          List[int]               # w             [len]           bit             .
    n:          int                     # n             -               -               .
    # len:        int                     # n_tag         -               Max Ext. Index  .
    q:          int                     # q             -               -               .
    log_n:      int                     # log_n         -               -               .
    k:          int                     # k             -               -               .
    # endregion

    def __init__(self, w, q: int = 2):
        if not isinstance(w, list):
            raise Exception("Input must be a list.")
        if q != 2:
            raise NotImplementedError()
        self.w = w
        self.n = len(w) + 1
        # self.len = 0
        self.q = q
        self.log_n = ceil(log(self.n, self.q))
        self.k = 2 * self.log_n + 2

    def encode(self, _debug_no_append=False):
        if not _debug_no_append:
            self.w.append(1)
            for i in range(self.log_n + 1):
                self.w.append(0)

        # self.len = len(self.w)
        print('w0     =', self.w)

        # Run algorithm
        self.eliminate()
        self.expand()

    def identical(self, i, j):
        for m in range(self.k):
            if self.w[i + m] != self.w[j + m]:
                return False
        return True

    def eliminate(self):
        found_identical_or_zero = True
        while found_identical_or_zero:
            found_identical_or_zero = False
            for i in range(len(self.w) - self.k):
                break_out = False
                for j in range(i + 1, len(self.w) - self.k + 1):
                    if not self.identical(i, j):
                        continue
                    found_identical_or_zero = True
                    for _ in range(self.k):
                        self.w.pop(i)
                    prepended = [0] + b(i, self.log_n) + b(j, self.log_n)
                    for p in reversed(prepended):
                        self.w.insert(0, int(p))
                    break_out = True
                    # assert(len(self.w) == self.len - 1)
                    # self.len = len(self.w)
                    print('w1     =', self.w)
                    break
                if break_out:
                    break
            if not found_identical_or_zero:
                found_zero_window = -1
                curr_length = 0
                for curr_index in range(len(self.w) - 1):
                    if self.w[curr_index] == 0:
                        curr_length += 1
                        if curr_length == self.log_n + 1:
                            found_zero_window = curr_index - self.log_n
                            break
                    elif self.w[curr_index] == 1:
                        curr_length = 0
                if found_zero_window >= 0:
                    for _ in range(self.log_n + 1):
                        self.w.pop(found_zero_window)
                    prepended = [1] + b(found_zero_window, self.log_n)
                    for p in reversed(prepended):
                        self.w.insert(0, int(p))
                    print('w2     =', self.w)
                    found_identical_or_zero = True

    def expand(self):
        while len(self.w) < self.n:
            # raise NotImplementedError()
            break
        self.w = self.w[:self.n]

    def output(self):
        return self.w
