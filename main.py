import contextlib
import io
import numpy as np
from encoder1 import *
from decoder1 import *
from utils import b


def run_test(w: List):
    assert(len(w) == n - int(alg_params['redundancy']))
    log_n = ceil(log(n, 2))
    orig_w = w.copy()
    print('n      =', n)
    print('log_n  =', log_n)
    print('k      =', 2 * log_n + 2)
    print('w      =', w)
    codeword = Encoder1().input(w).encode().output()
    print('output =', codeword)
    decodeword = Decoder1().input(codeword).decode().output()
    print('decode =', decodeword)
    if orig_w == decodeword:
        print('EQUAL')
        return True
    return False


def run_main():
    len_source = number_of_tests + n - 1 - int(alg_params['redundancy'])
    ones_in_source = int(len_source * average_percent_of_ones)
    arr = np.array([1] * ones_in_source + [0] * (len_source - ones_in_source))
    np.random.shuffle(arr)
    source = list(arr)
    number_of_successes = 0
    for i in range(number_of_tests):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            res = run_test(source[i:i + (n - int(alg_params['redundancy']))])
        out = f.getvalue()
        # if i & 0b1111111 == 0:  # Print every 128-th output
        #     print(out)
        number_of_successes += res
    print('r      =', int(alg_params['redundancy']))
    print('rll+   =', int(alg_params['rll_extra']))
    print("Succeeded {} times out of {} ({}%)".format(number_of_successes, number_of_tests,
                                                      100. * number_of_successes / number_of_tests))


# TEST PARAMETERS
n = 2 ** 7                      # Remember: Input is of length (n - redundancy) (good choice: 2 ** 8)
number_of_tests = 2 ** 6        # Two consecutive tests u, v satisfy u[1:] == v[:-1] (good choice: 2 ** 9)
average_percent_of_ones = 0.35   # As this gets closer to 0.5, less iterations are needed (good choice: 0.1)
if __name__ == '__main__':
    alg_params['redundancy'] = 1; alg_params['rll_extra'] = 2; run_main()
    alg_params['redundancy'] = 2; alg_params['rll_extra'] = 1; run_main()
    alg_params['redundancy'] = 2; alg_params['rll_extra'] = 2; run_main()
    alg_params['redundancy'] = 1; alg_params['rll_extra'] = 1; run_main()

# region Anecdotes

# Before inlining 'identical', profiling shows:
# When n=256, number_of_tests=512, the method 'identical' is called 142M times (~ 2^27), and the program takes 109sec.
# So for one test, on average, it is called 2^(27-9)=2^18 times. Since n=2^8, we expected a lot more times...
# After inlining 'identical', profiling shows:
# Now it takes 78sec (diff=31sec). This means that one test on average takes around 150msec.
# According to Competitive Programming, 100M operations happen in 1 sec, so here, we have 15M operations.
# Since n=2^8, we expected 2^(8*3+2*2)=2^28 which is roughly 256M operations...

# endregion
