from math import log, ceil
from utils import *

# from encoder import alg_params

"""

Decoder works like this:
Input: w of length n.
Output: D(w) of length (n - 1).
(1) Search for a (log_n + 1)-long run of zeros.
    (1.1) If found:  w = w' * 1 * 0^(log_n + 1) * w''.   (Proof for both: Recall that (1 * 0^(log_n + 1)) was appended.
    (1.2) Otherwise: w = w' * 1 * 0^t, where (0 <= t <= log_n).           These zeros are never victims of phase 2.)
(2) Update: w <- w' * 1 * 0^(log_n + 1)
(3) Do until len(w) == (n + log_n + 1):
    (3.1) If w[0] == 0, undo phase 1 on w.
    (3.2) Otherwise, undo phase 2 on w.
(4) Return w[:(n - 1)]

Data Structures and Complexity:
(1) One way is to convert the input into a dictionary, so that random-access is O(log_n).
    Time complexity:  O(ITERATIONS * UPDATE TIME PER ITERATION) = O((n * log_n) * (log_n * log_n)) = O(n * log^3_n)
    Space complexity: O(n)
(2) Another way, maintaining O(log_n) space complexity, is to insert with O(n) time complexity.
    Time complexity:  O(ITERATIONS * UPDATE TIME PER ITERATION) = O((n * log_n) * (n * log_n)) = O(n^2 * log^2_n)
    Space complexity: O(log_n)
This file implements option 2.

"""


class Decoder:
    # region Parameters
    w: List[int]
    n: int
    q: int
    log_n: int
    k: int
    start_index: int
    end_index: int
    zero_rll: int
    redundancy: int

    # endregion

    def __init__(self, alg_params, verbose_mode, q: int = 2):
        self.q = q
        self.alg_params = alg_params
        self.verbose = verbose_mode

    def input(self, w: List):
        self.w = w
        self.redundancy = int(self.alg_params['redundancy'])
        self.n = len(w)
        self.log_n = ceil(log(self.n, self.q))
        self.k = 2 * self.log_n + 2
        self.zero_rll = self.log_n + int(self.alg_params['rll_extra'])
        self.start_index = 0
        self.end_index = self.n
        return self

    def decode(self):
        self.start_index = 0
        self.end_index = self.n - 1

        # Search for a (log_n + rll_extra)-long run of zeros, or the last run of zeros
        curr_length = 0
        for curr_index in range(len(self.w)):
            if self.w[curr_index] == 0:
                curr_length += 1
                if curr_length == self.zero_rll:
                    self.end_index = curr_index - self.zero_rll
                    break
            else:  # if self.w[curr_index] != 0:
                curr_length = 0

        # If not found, make one at the end (this is needed - it might be that some removed windows are among them)
        # Proof of need: Codeword = [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0] (run it to see)
        last_run = 0
        while self.w[self.end_index] == 0:
            last_run += 1
            self.end_index -= 1
        self.w.extend([0] * (self.zero_rll - last_run))

        # At this point, w[:self.end_index] is w' from the decoder description above
        # The relevant part of w is maintained to be w[self.start_index:self.end_index]
        # Note: The right-side limit (self.end_index) is exclusive
        if self.verbose:
            print('w-0    =', self.w[self.start_index:self.end_index + self.zero_rll + 1])
        # print('wstart =', self.start_index)
        # print('wend   =', self.end_index)
        while (self.end_index - self.start_index) < (self.n - 1):
            phase = self.w[self.start_index]
            self.start_index += 1
            if phase == 0:
                self.undo_phase1()
                if self.verbose:
                    print('w-1    =', self.w[self.start_index:self.end_index + self.zero_rll + 1])
            elif phase == 1:
                self.undo_phase2()
                if self.verbose:
                    print('w-2    =', self.w[self.start_index:self.end_index + self.zero_rll + 1])
        if self.verbose:
            print('dec*   =', self.w[self.start_index:self.end_index])
        if int(self.alg_params['redundancy']) == 2:
            while self.w[self.start_index] == 1:
                # Are we done yet?
                self.start_index += 1
                self.undo_phase2()
                if self.verbose:
                    print('w-2*   =', self.w[self.start_index:self.end_index])
        assert (self.end_index - self.start_index) == (self.n - 1)
        return self

    def undo_phase1(self):
        index1 = q_ary_rev(self.w[self.start_index:self.start_index + self.log_n], self.q)
        self.start_index += self.log_n
        index2 = q_ary_rev(self.w[self.start_index:self.start_index + self.log_n], self.q)
        self.start_index += self.log_n

        # index2 is the index of the second window, BEFORE removing the first window
        index2 -= self.k

        # Might make an animation or an illustration that explains this - I love it!
        for _ in range(self.k):
            self.w.insert(self.start_index + index1, self.w[self.start_index + index2 + self.k - 1])

        self.end_index += self.k

    def undo_phase2(self):
        index = q_ary_rev(self.w[self.start_index:self.start_index + self.log_n], self.q)
        self.start_index += self.log_n

        # Set slice in list - this takes O(SLICE SIZE + LIST LENGTH) = O(n)
        self.w[(self.start_index + index):(self.start_index + index)] = [0] * self.zero_rll
        self.end_index += self.zero_rll

    def output(self):
        return self.w[self.start_index + int(self.alg_params['redundancy']) - 1:self.end_index]
