"""
Tests for Fibonacci Sequence.
"""

from typing import Callable, Dict, List
from printer import print_fail, print_pass
from leetcode_509_fibonacci_sequence import fibonacci


def test_fibonacci_sequence(func: Callable[[int], int], n: int, expected: int) -> None:
    """Print custom output for failing or passing tests."""
    if func(n) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


def main(tests: List[Dict]) -> None:
    """Test function."""
    for i, test in enumerate(tests, start=1):
        n: int = test['n']
        expected: int = test['expected']
        ans = fibonacci(n)

        print(f"Test #{i}")
        print(f"Input: n = {n}")
        print(f"Expected Output: {expected}")
        print(f"My answer: {ans}")

        test_fibonacci_sequence(fibonacci, n, expected)
        print()


if __name__ == "__main__":
    tests = [
        {
            'n': 0,
            'expected': 0
        },
        {
            'n': 1,
            'expected': 1
        },
        {
            'n': 5,
            'expected': 5
        },
        {
            'n': 10,
            'expected': 55
        },
        {
            'n': 50,
            'expected': 12586269025
        },
        {
            'n': -1,
            'expected': -1
        },
        {
            'n': 2.5,
            'expected': -1
        },
        {
            'n': 100,
            'expected': 354224848179261915075
        }
    ]

    main(tests)
