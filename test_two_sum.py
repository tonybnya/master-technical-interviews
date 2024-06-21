"""
Tests for Two Sum problem.
"""

from typing import Callable, Dict, List, Union

from dsa_two_sum import two_sum

from printer import print_fail, print_pass


def test_two_sum(
    func: Callable[[List[int], int], Union[int, str]],
    arr: List[int],
    target: int,
    expected: List[int],
) -> None:
    """
    Printer Function for Two Sum Problem.
    """
    if func(arr, target) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


def main(tests: List[Dict]) -> None:
    """
    Tests function
    """
    for i, test in enumerate(tests, start=1):
        arr: List[int] = test["arr"]
        target: int = test["target"]
        expected: List[int] = test["expected"]
        ans: List[int] = two_sum(arr, target)

        print(f"Test #{i}")
        print(f"Input: arr = {arr}, target = {target}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        test_two_sum(two_sum, arr, target, expected)
        print()


if __name__ == "__main__":
    tests: List[Dict] = [
        {"arr": [3, 3], "target": 6, "expected": [0, 1]},
        {"arr": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"arr": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"arr": [5, 3, 7, 10, 1], "target": 17, "expected": [2, 3]},
        {"arr": [5, 3, 6, 10, 1], "target": 17, "expected": "No Two Sum Solution"},
    ]

    main(tests)
