from math import log, ceil
from utils import *

"""

n * log_n       iterations
n   OR?  log_n  new windows need to be compared per iteration
n               comparisons for each window
log_n           operations for each comparison

TOTAL: n^3 * (log_n)^2  [ OR?  n^2 * (log_n)^3 ] <-- The latter case does not seem to be right...

TIME                       SPACE
-----                      -----
  n^3 * (log_n)^2    |       log_n          # this file
  n^2 * log_n        |       n * log_n      # must be similar to crazy_algorithm.py, but forgot
  n   * (log_n)^2    |       n^2            # see crazy_algorithm1.py (the queue has issues, though...)

"""


class Algorithm1:
    # region Parameters
    # FIELD     TYPE                    SKETCH NAME     DESCRIPTION
    w:          List[int]               # w             .
    n:          int                     # n             .
    q:          int                     # q             .
    log_n:      int                     # log_n         .
    k:          int                     # k             .
    # endregion

    def __init__(self, q: int = 2):
        if q != 2:
            raise NotImplementedError()
        self.q = q

    def input(self, w, is_codeword=False):
        if not isinstance(w, list):
            raise Exception("Input must be a list.")
        # Tested: `self.w = w` happens by reference (since `list` is mutable)
        self.w = w
        self.n = len(w) + (not is_codeword)
        self.log_n = ceil(log(self.n, self.q))
        self.k = 2 * self.log_n + 2
        return self

    def encode(self, _debug_no_append=False):
        if not _debug_no_append:
            self.w.append(1)
            for i in range(self.log_n + 1):
                self.w.append(0)
        print('w0     =', self.w)

        # Run algorithm
        return self.eliminate().expand()

    def eliminate(self):
        found_identical_or_zero = True
        while found_identical_or_zero:
            found_identical_or_zero = False
            for i in range(len(self.w) - self.k):
                break_out = False
                for j in range(i + 1, len(self.w) - self.k + 1):
                    if self.w[i:i + self.k] != self.w[j:j + self.k]:  # not self.identical(i, j):
                        continue
                    found_identical_or_zero = True
                    for _ in range(self.k):
                        self.w.pop(i)
                    prepended = [0] + b(i, self.log_n) + b(j, self.log_n)
                    for p in reversed(prepended):
                        self.w.insert(0, int(p))
                    break_out = True
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
                    # We are taking our time, popping in O(found_zero_window * log_n) = O(n * log_n)
                    for _ in range(self.log_n + 1):
                        self.w.pop(found_zero_window)

                    # One-by-one appending in O(len(appended))
                    prepended = [1] + b(found_zero_window, self.log_n)
                    for p in reversed(prepended):
                        self.w.insert(0, int(p))
                    found_identical_or_zero = True
                    print('w2     =', self.w)
        return self

    def expand(self):
        while len(self.w) < self.n:
            # Go over all words of length log_n in O(n) time, and for each word,
            # check that it does not exist in w in O(n * log_n) time,
            # and that it is not equal to some Cr_log_n(w[-i]) in O(log^2_n * log_log_n) time.
            # Total: O(n * (n * log_n + log^2_n * log_log_n)) = O(n^2 * log_n) time.
            # Space: O(log_n) additional space.

            # FIXME: The following is a shortcut for the binary case
            assert(self.q == 2)

            # u is a binary word of length log_n
            good_u: Optional[List] = None
            for u in range(self.n):
                next_u = False
                bin_u = [int(p) for p in b(u, self.log_n)]
                for curr in range(len(self.w) - self.log_n + 1):
                    if bin_u == self.w[curr:curr + self.log_n]:
                        next_u = True
                        break
                    # print('Truly,', self.w[curr:curr + self.log_n], 'does not equal', bin_u)
                if next_u:
                    continue
                for i in range(1, self.log_n):
                    cr_i = cr(self.log_n, self.w[-i:])
                    if bin_u == cr_i:
                        next_u = True
                        break
                    # print('Truly,', cr_i, 'does not equal', bin_u)
                if next_u:
                    continue
                good_u = bin_u
                # print("good_u =", good_u)
                break
            if good_u is None:
                raise Exception("B contains all words of length log_n.")
            self.w.extend(good_u)
            print('w+     =', self.w)
        return self

    def output(self):
        # O(n) place for the output only
        return self.w[:self.n]

    def decode(self):
        raise NotImplementedError()
