"""
Leetcode 258. Add Digits

Given an integer num, repeatedly add all its digits until the result
has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
"""

from __future__ import annotations

from typing import Callable

from digits_sum import digits_sum
from printer import print_fail, print_pass


def add_digits(num: int) -> int:
    """Add digits until the result has only one digit."""
    digits: tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    if num in digits:
        return num

    num: int = digits_sum(num)

    return add_digits(num)


def optimal(num: int) -> int:
    """Optimal Solution."""
    if num == 0:
        return 0

    return 9 if num % 9 == 0 else num % 9


def tester(func: Callable[[int], int], num: int, expected: int) -> None:
    """Print custom output for testing."""
    if func(num) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        num_str, expected_str = line.strip().split()

        num: int = int(num_str)
        expected: int = int(expected_str)

        ans = optimal(num)

        print(f"Input: num = {num}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        tester(optimal, num, expected)
        print()
