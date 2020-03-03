from math import log, ceil
from typing import Optional, List, NewType, Tuple
from autoinc_queue import AutoIncQueue
from avl_rank import AvlRankTree as DeltaTree, AvlRankTree as AvlTree
from hashtable import ChainedHashtable as Hashtable, LinkedList, Link

""" Data Classes from Python 3.7 are AMAZING
from dataclasses import dataclass, field

@dataclass
class Window:
    values: List[int] = field(default_factory=list)
    index: int = field(default=0, compare=False)
"""


# User-defined types
bit = NewType('bit', int)
window = NewType('window', Tuple[bit, ...])


def cr(n, w):
    out = w
    while len(out) < n:
        out += w


class Algorithm1:
    # FIELD     TYPE                    SKETCH NAME     DOMAIN          RANGE           DESCRIPTION
    input:      List[bit]               # s             [n]             bit             .
    w:          List[bit]               # w             [len]           bit             .
    n:          int                     # n             -               -               .
    len:        int                     # n_tag         -               Max Ext. Index  .
    q:          int                     # q             -               -               .
    log_n:      int                     # log_n         -               -               .
    k:          int                     # k             -               -               .
    index_in:   Optional[DeltaTree]     # M             Ext. Index      Int. Index      .
    index_ex:   Optional[LinkedList]    # L             Int. Index      Ext. Index      .
    windows:    Optional[Hashtable]     # W             window          Link@index_ex   .
    windows_id: Optional[AvlTree]       # I             Int. Index      Link@windows    .
    queue:      Optional[AutoIncQueue]  # Q             -               Ext. Index      .

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
        self.index_in = None
        self.index_ex = None
        self.windows = None
        self.windows_id = None
        self.queue = None

    def window_at(self, j_ex) -> Optional[window]:
        if j_ex < 0 or j_ex + self.k - 1 >= self.len:
            return None
        # Tuple is a hashable immutable object, best for using as key
        return window(tuple(self.w[j_ex:j_ex + self.k - 1]))

    def encode(self):
        w_list = self.input + [bit(1)] + ([bit(0)] * (self.log_n + 1))
        # TODO: Make self.w a LinkedList so that removal of a window is O(k)
        self.w = LinkedList(iterator=w_list)

        self.len = len(self.w)

        # Initialize data structures (see README for details)
        self.index_in = DeltaTree()
        self.index_ex = LinkedList()
        self.windows = Hashtable(self.len)
        self.windows_id = AvlTree()
        self.queue = AutoIncQueue(range(self.len), increment_until=self.len)

        # Run algorithm
        self.eliminate()
        self.expand()

    def eliminate(self):
        while True:
            # TODO: Maintain a current node on input and use queue.prev to know
            #       whether to jump to next or to jump to head.
            #       This is so that the removal of a window is O(k)
            input_iter = None

            if not self.queue.empty():
                # There are more windows to check
                j_ex = self.queue.pop()
                win_j: Optional[window] = self.window_at(j_ex)
                if win_j is None:
                    # TODO: Windows done, check (log_n + 1)-RLL
                    raise NotImplementedError()

                index_ex_link: Optional[Link] = self.windows.get(win_j)
                if index_ex_link is None:
                    # New window who dis
                    j_in = self.index_in[j_ex]
                    link_index_ex = Link(j_in, j_ex)
                    self.index_ex.push(link_index_ex, prev=self.index_ex.tail)
                    link_window = self.windows.put(win_j, link_index_ex)
                    self.windows_id.insert(j_in, link_window)
                    # TODO: Continue according to the algorithm described in my sketch paper labeled: ( * This * )
                else:
                    i_in, i_ex = index_ex_link.key, index_ex_link.value
                    # j_in = self.index_in[j_ex]
                    self.index_in.delta_add(i_ex + self.k - 1, self.len, 1)
                    self.index_in.delta_add(0, i_ex + self.k - 2, -(self.k - 1))
                    min_in = self.index_ex.head.key
                    self.queue.extend(range(self.k - 2, -1, -1))

                    # for i, key in enumerate(range(min_in - self.k + 1, min_in)):
                    #     link_index_ex = Link(i, key)
                    #     self.index_ex.push(link_index_ex, prev=None)
                    #     self.windows_id
                    #     self.windows
            else:  # Queue is empty: either RLL, case 2 or done
                pass

    def expand(self):
        while len(self.w) < self.n:
            raise NotImplementedError()
        self.w = self.w[:self.n]

    def output(self):
        return self.w

    def handle_primal_identical(self, i, j):
        # TODO: This is old. Kill your darling and start from zero.
        # Step 0:
        # From the internal indexing perspective, i and j might satisfy i > j
        # This might be the case when a newly-added window at the beginning of self.w exists in the already-seen input
        # So let us ensure i < j
        assert i != j
        if i > j:
            i = i ^ j
            j = i ^ j
            i = i ^ j

        # Step 1:
        # Move (internal) indices [0, i - 1] to [k - 1, i + k - 2]
        return self.w + i  # Just to suppress IDE complaints

        # Step 2:

        pass
