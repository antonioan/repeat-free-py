import contextlib
import io
import numpy as np
from algorithm1 import *
from utils import b


def run_test(w):
    assert(len(w) == n - 1)
    log_n = ceil(log(n, 2))
    print('n      =', n)
    print('log_n  =', log_n)
    print('k      =', 2 * log_n + 2)
    print('w      =', w)
    print('output =', Algorithm1().input(w).encode().output())


# TEST PARAMETERS
n = 2 ** 8  # Remember: Input is of length (n - 1)
number_of_tests = 2 ** 9  # By the way they are created, two consecutive test inputs u, v satisfy u[1:] == v[:-1]
average_percent_of_ones = 0.1  # As this gets closer to 0.5, less iterations are needed
if __name__ == '__main__':
    len_source = number_of_tests + n - 2
    ones_in_source = int(len_source * average_percent_of_ones)
    arr = np.array([1] * ones_in_source + [0] * (len_source - ones_in_source))
    np.random.shuffle(arr)
    source = list(arr)
    for i in range(number_of_tests):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            run_test(source[i:i + (n - 1)])
        out = f.getvalue()
        if i & 0b1111111 == 0:  # Print every 128-th output
            print(out)

# Before inlining 'identical', profiling shows:
# When n=256, number_of_tests=512, the method 'identical' is called 142M times (~ 2^27), and the program takes 109sec.
# So for one test, on average, it is called 2^(27-9)=2^18 times. Since n=2^8, we expected a lot more times...
# After inlining 'identical', profiling shows:
# Now it takes 78sec (diff=31sec). This means that one test on average takes around 150msec.
# According to Competitive Programming, 300M operations happen in 1 sec, so here, we have 45M operations.
# Since n=2^8, we expected 2^(8*3+2)=2^26 which is roughly 64M operations.

