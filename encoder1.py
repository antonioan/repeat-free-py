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


# Where do we go now?
  1. Better time complexity (but worse space)     <- Most important
>       TODO: Finish third implementation
x 2. q-ary support                                <- Between easy and important
> 3. Decoder                                      <- Easiest

"""

alg_params = {'redundancy': 1, 'rll_extra': 2}


class Encoder1:
    # region Parameters
    w:              List[int]
    n:              int
    q:              int
    log_n:          int
    k:              int
    zero_rll:       int
    # endregion

    def __init__(self, q: int = 2):
        if q != 2:
            raise NotImplementedError()
        assert 1 <= int(alg_params['redundancy']) <= 2
        assert 1 <= int(alg_params['rll_extra']) <= 2
        self.q = q

    def input(self, w: List):
        # Tested: `self.w = w` happens by reference (since `list` is mutable)
        self.w = w
        self.n = len(w) + int(alg_params['redundancy'])
        self.log_n = ceil(log(self.n, self.q))
        self.k = 2 * self.log_n + 2
        self.zero_rll = self.log_n + int(alg_params['rll_extra'])
        return self

    def encode(self, _debug_no_append=False):
        if int(alg_params['redundancy']) == 2:
            self.w.insert(0, 0)
        if not _debug_no_append:
            self.w.append(1)
            for i in range(self.zero_rll):
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
                    self.w[i:i+self.k] = []
                    prepended = [0] + b(i, self.log_n) + b(j, self.log_n)
                    for p in reversed(prepended):
                        self.w.insert(0, int(p))
                    break_out = True
                    print('w1     =', self.w)
                    break
                if break_out:
                    break
            if not found_identical_or_zero:
                zero_window_index = -1
                curr_length = 0
                for curr_index in range(len(self.w) - 1):
                    if self.w[curr_index] == 0:
                        curr_length += 1
                        if curr_length == self.zero_rll:
                            zero_window_index = curr_index - self.zero_rll + 1
                            break
                    elif self.w[curr_index] == 1:
                        curr_length = 0
                if zero_window_index >= 0:
                    self.w[zero_window_index:zero_window_index + self.zero_rll] = []

                    # One-by-one appending in O(len(appended))
                    prepended = [1] + b(zero_window_index, self.log_n)
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
