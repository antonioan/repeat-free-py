from math import log, ceil
from typing import Iterable, Optional
from avl_rank import AvlRankTree  # OR: from avl import AvlTree
from queue import Queue
from fenwick import FenwickTree


class Window(list):
    # Note: Comparison is via list.__lt__(), which compares lexicographically.
    def __init__(self, values: Iterable[int], pos):
        list.__init__(self, values)
        self.pos = pos


class Algorithm1(object):
    def __init__(self, s, q: int = 2):
        if not isinstance(s, list):
            raise Exception("Input must be a list.")
        if q != 2:
            raise NotImplementedError()
        self.input = s
        self.n = len(s) + 1
        self.q = q
        self.log_n = ceil(log(self.n, self.q))
        self.k = 2 * self.log_n + 2
        self.w = []
        self.windows: Optional[AvlRankTree] = None
        self.queue: Optional[Queue] = None
        self.real_ids: Optional[FenwickTree] = None

    def encode(self):
        self.w = self.input + [1] + ([0] * (self.log_n + 1))
        w_len = len(self.w)

        # Initialize data structures (see README for details)
        self.windows = AvlRankTree()
        self.queue = Queue(range(w_len), increment_until=w_len)
        self.real_ids = FenwickTree(arr=range(w_len))

        # Run algorithm
        self.eliminate()
        self.expand()

    def eliminate(self):
        while True:
            if len(self.queue) > 0:
                # There are more windows to check
                j_internal = self.queue.pop()
                j = self.real_ids[j_internal]
                win_j = Window(self.w[j:j + self.k], j_internal)
                exists, existent_key = self.windows.find(win_j)
                if not exists:
                    # New window who dis
                    self.windows.add(win_j)
                else:
                    # Una problema, signore
                    win_i: Window = existent_key
                    i_internal = win_i.pos
                    self.handle_primal_identical(i_internal, j_internal)
            else:  # Queue is empty: either case 2 or done
                pass

    def expand(self):
        while len(self.w) < self.n:
            raise NotImplementedError()
        self.w = self.w[:self.n]

    def output(self):
        return self.w

    @staticmethod
    def cr(n, w):
        out = w
        while len(out) < n:
            out += w

    def handle_primal_identical(self, i, j):
        # Step 0:
        # From the internal indexing perspective, i and j might satisfy i > j
        # This is the case when a newly-added window at the beginning of self.w exists in the already-processed input
        # So let us ensure i < j
        assert i != j
        if i > j:
            i = i ^ j
            j = i ^ j
            i = i ^ j

        # Step 1:
        # Move (internal) indices [0, i - 1] to [k - 1, i + k - 2]
        self.real_ids.add_range(0, i - 1, self.k - 1)

        # Step 2:
        #

        pass
