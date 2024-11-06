# -*- coding: utf-8 -*-
import operator


def apply_delta_v1(input, delta, minn, maxn):
    # Modifies an input number by a delta, ensuring the result stays within bounds.
    # First attempt (showing my process). Obsolesced by apply_delta
    boundary = minn if delta < 0 else maxn
    comp = operator.ge if delta < 0 else operator.le
    if (comp(input + delta, boundary)):
        result = input + delta
    else:
        result = boundary
    return result


def apply_delta(input, delta, minn, maxn):
    # Modifies an input number by a delta, ensuring the result stays within bounds.
    return max(min(maxn, input + delta), minn)


def assert_test_results(successes, failures):
    # Assert test results do not include any failures. Report only failures if any
    # are found. Report all successes if no failures are found.
    assert len(failures) == 0, "\n" + "\n".join(failures) + Color.RED + f"\n\n{len(failures)} test failures.\n" + Color.END
    print("\n".join(successes) + Color.GREEN + f"\n\n{len(successes)} tests passed." + Color.END)


class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    CYAN = '\033[96m'
