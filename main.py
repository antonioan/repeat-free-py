import argparse
import contextlib
import fileinput
import io
import sys

import numpy as np
from encoder import *
from decoder import *


# Straight-forward check that there are no two identical windows of length k in the sequence, for testing purposes
def validate_no_identical_windows(w, k):
    seen_windows = set()
    for i in range(len(w) - k + 1):
        hw = hash_window(w[i:i + k])
        if hw in seen_windows:
            return False
        else:
            seen_windows.add(hw)
    return True


def run_test(w: List, action, redundancy, complexity_mode, verbose_mode, test_mode):
    alg_params = {'redundancy': redundancy, 'rll_extra': 2 - redundancy}
    n = len(w) + int(alg_params['redundancy'])
    if test_mode:
        assert (len(w) == n - int(alg_params['redundancy']))
    orig_w = w.copy()
    log_n = ceil(log(n, 2))
    k = 2 * log_n + 2
    if verbose_mode:
        print('n      =', n)
        print('log_n  =', log_n)
        print('k      =', k)
        print('w      =', w)

    res_word = Encoder(complexity_mode, verbose_mode, alg_params).input(
        w).encode().output() if action == "encode" else Decoder(alg_params, verbose_mode).input(
        w).decode().output()

    print('output =', "".join([str(x) for x in res_word]))

    if test_mode:
        if action == "encode":
            if validate_no_identical_windows(res_word, k):
                print('TEST SUCCESS')
                return True
            else:
                print('TEST FAILED!')
                print('result is not repeat free')
                return False
        elif action == "decode":
            if orig_w == Encoder(complexity_mode, False, alg_params).input(w).encode().output():
                print('TEST SUCCESS')
                return True
            else:
                print('TEST FAILED!')
                print('Encode(Decode(w)) != w')
    return True


# def run_main(print_output=False):
#     len_source = number_of_tests + n - 1 - int(alg_params['redundancy'])
#     ones_in_source = int(len_source * average_percent_of_ones)
#     arr = np.array([1] * ones_in_source + [0] * (len_source - ones_in_source))
#     np.random.shuffle(arr)
#     source = list(arr)
#     number_of_successes = 0
#     for i in range(number_of_tests):
#         f = io.StringIO()
#         with contextlib.redirect_stdout(f):
#             res = run_test(source[i:i + (n - int(alg_params['redundancy']))])
#         out = f.getvalue()
#         if print_output and i & 0b1111111 == 0:  # Print every 128-th output
#             print(out)
#         number_of_successes += res
#     print('r      =', int(alg_params['redundancy']))
#     print('rll+   =', int(alg_params['rll_extra']))
#     print("Succeeded {} times out of {} ({}%)".format(number_of_successes, number_of_tests,
#                                                       100. * number_of_successes / number_of_tests))


if __name__ == '__main__':
    parser = argparse.ArgumentParser("./main")
    parser.add_argument("action", help="{encode, decode}")
    parser.add_argument("-i", "--input", help="get word from standard input", action="store_true")
    parser.add_argument("sequence", nargs="?", help="a binary word")
    parser.add_argument("-r", "--redundancy", type=int, choices=[1, 2],
                        help="how many redundancy bits to use", default=1)
    parser.add_argument("-c", "--complexity", choices=["time", "space"],
                        help="save time or space complexity", default="time")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-t", "--test", help="test for output correctness", action="store_true")
    args = parser.parse_args()

    if args.sequence is None:
        if args.input:  # get word from standard input
            args.sequence = input()
        else:
            print("You must enter a word either from the command line or via standard input", file=sys.stderr)
            exit()

    run_test([int(x) for x in list(args.sequence)], args.action, args.redundancy, args.complexity, args.verbose,
             args.test)

# region Anecdotes

# Before inlining 'identical', profiling shows:
# When n=256, number_of_tests=512, the method 'identical' is called 142M times (~ 2^27), and the program takes 109sec.
# So for one test, on average, it is called 2^(27-9)=2^18 times. Since n=2^8, we expected a lot more times...
# After inlining 'identical', profiling shows:
# Now it takes 78sec (diff=31sec). This means that one test on average takes around 150msec.
# According to Competitive Programming, 100M operations happen in 1 sec, so here, we have 15M operations.
# Since n=2^8, we expected 2^(8*3+2*2)=2^28 which is roughly 256M operations...

# endregion
