# -*- coding: utf-8 -*-
from util import Color, apply_delta, assert_test_results


def test__apply_delta():
    def generate_test_cases(boundary):
        minn, maxn = boundary        
        mean = (minn + maxn) // 2
        test_cases = [
            # mid range
            ("-5 delta", (mean, -5, minn, maxn), mean - 5),
            ("-1 delta", (mean, -1, minn, maxn), mean - 1),
            ("0 delta", (mean, 0, minn, maxn), mean),
            ("1 delta", (mean, 1, minn, maxn), mean + 1),
            ("5 delta", (mean, 5, minn, maxn), mean + 5),

            # low boundary
            ("low boundary achieved: -2 delta", (minn + 2, -2, minn, maxn), minn),
            ("low boundary achieved: -1 delta", (minn + 1, -1, minn, maxn), minn),
            ("low boundary isn't crossed: -2 delta", (minn + 1, -2, minn, maxn), minn),
            ("low boundary isn't crossed: -1 delta", (minn, -1, minn, maxn), minn),
            ("low boundary isn't crossed: 0 delta", (minn, 0, minn, maxn), minn),
            ("low boundary recovery: 1 delta", (minn, 1, minn, maxn), minn + 1),

            # high boundary
            ("high boundary achieved: 2 delta", (maxn - 2, 2, minn, maxn), maxn),
            ("high boundary achieved: 1 delta", (maxn - 1, 1, minn, maxn), maxn),
            ("high boundary isn't crossed: 2 delta", (maxn - 1, 2, minn, maxn), maxn),
            ("high boundary isn't crossed: 1 delta", (maxn, 1, minn, maxn), maxn),
            ("high boundary isn't crossed: 0 delta", (maxn, 0, minn, maxn), maxn),
            ("high boundary recovery: -1 delta", (maxn, -1, minn, maxn), maxn - 1)
        ]
        # prefix description with range
        def prefix_range(test_case):
            return (Color.CYAN + f"range {minn} to {maxn}: " + Color.YELLOW + test_case[0] + Color.END,) + test_case[1:]

        return map(prefix_range, test_cases)

    # replicate test cases across min/max sets
    boundaries = [(-100, -50), (-50, 0), (-50, 50), (0, 50), (50, 100)]
    test_sets = map(generate_test_cases, boundaries)
    
    successes = []
    failures = []    
    for test_set in test_sets:
        for case_name, args, expected in test_set:
            actual = apply_delta(*args)
            try:
                assert actual == expected
                successes.append(Color.GREEN + "pass" + Color.END + f": {case_name} (expected: {expected})")
            except:
                failures.append(Color.RED + "FAIL" + Color.END + f": {case_name} (actual: {actual}, expected: {expected})")

    assert_test_results(successes, failures)


if __name__ == "__main__":
    test__apply_delta()
