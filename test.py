import numpy as np
import contextlib
import io

from main import do_action


def run_tests(number_of_tests, n, average_percent_of_ones, redundancy, print_output):
    len_source = number_of_tests + n - 1 - redundancy
    ones_in_source = int(len_source * average_percent_of_ones)
    arr = np.array([1] * ones_in_source + [0] * (len_source - ones_in_source))
    np.random.shuffle(arr)
    source = list(arr)
    number_of_successes = 0
    for i in range(number_of_tests):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            w = source[i:i + (n - redundancy)]
            res = do_action(w, 'encode', redundancy, 'time', True, True)
        out = f.getvalue()
        if print_output and i & 0b1111111 == 0:  # Print every 128-th output
            print(out)
        number_of_successes += res
    print("With n={}, r={}, p_ones={},".format(n, redundancy, average_percent_of_ones))
    print("Succeeded {} times out of {} ({}%)".format(number_of_successes, number_of_tests,
                                                      100. * number_of_successes / number_of_tests))


if __name__ == '__main__':
    run_tests(
        number_of_tests=2 ** 10,
        n=2 ** 7,
        average_percent_of_ones=0.35,
        redundancy=2,
        print_output=True
    )
