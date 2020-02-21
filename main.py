from fenwick import FenwickTree

test_silent = 1


def test_print(i, b):
    if test_silent == 0:
        print("TEST", "PASSED" if b else "FAILED", "- fenwick", i)
    return b


def test_fenwick():
    tests_passed = 0
    arr = [1, 2, 3, 4, 5]
    tree = FenwickTree(arr=arr)
    tests_passed += test_print(1, tree == [1, 2, 3, 4, 5])
    tree.add_range(1, 3, -2)
    tests_passed += test_print(2, tree == [1, 0, 1, 2, 5])
    tests_passed += test_print(3, tree[1] == 0)
    if tests_passed == 3:
        print("Congrats! All tests for fenwick passed.")
    else:
        print("Sorry...")


def test_all():
    test_fenwick()


if __name__ == '__main__':
    seq = [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
    fenwick = FenwickTree(arr=seq)
    print(fenwick.values)
    print(seq[-4:])
