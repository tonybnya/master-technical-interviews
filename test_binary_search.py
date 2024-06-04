"""
Tests for Binary Search Algorithm.
"""

from binary_search import search
from printer import print_fail, print_pass
from typing import Callable, Dict, List, Union


def test_binary_search(func: Callable[[List[int], int], int], arr: List[int], target: int, expected: int) -> None:
    """
    Printer Function for Binary Search Algorithm.
    """
    if func(arr, target) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


def main(tests: List[Dict]) -> None:
    """
    Tests Function
    """
    for i, test in enumerate(tests, start=1):
        arr: List[int] = test['arr']
        target: int = test['target']
        expected: int = test['expected']
        ans: int = search(arr, target)

        print(f"Test #i")
        print(f"Input: arr = {arr}, target = {target}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        test_binary_search(search, arr, target, expected)
        print()


if __name__ == "__main__":
    tests: List[Dict] = [
        {
            'arr': [1, 3, 5, 7, 10, 13, 17, 21, 32, 53],
            'target': 5,
            'expected': 2
        },
        {
            'arr': [1, 3, 5, 7, 10, 13, 17, 21, 32, 53],
            'target': 1,
            'expected': 0
        },
        {
            'arr': [1, 3, 5, 7, 10, 13, 17, 21, 32, 53],
            'target': 53,
            'expected': 9
        },
        {
            'arr': [1, 3, 5, 7, 10, 13, 17, 21, 32, 53],
            'target': 8,
            'expected': -1
        },
        {
            'arr': [],
            'target': 5,
            'expected': -1
        },
        {
            'arr': [10],
            'target': 10,
            'expected': 0
        },
        {
            'arr': [10],
            'target': 5,
            'expected': -1
        },
        {
            'arr': [1, 3, 5, 5, 5, 7, 10],
            'target': 5,
            'expected': 3
        },
        {
            'arr': [1, 3, 5, 5, 5, 7, 10],
            'target': 6,
            'expected': -1
        }
    ]

    main(tests)
