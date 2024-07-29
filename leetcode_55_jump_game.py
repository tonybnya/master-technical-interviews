"""
Leetcode 55. Jump Game

You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length
at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps
to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach
the last index.
"""

from __future__ import annotations

from typing import Callable

from printer import print_fail, print_pass


def jump_game(nums: list[int]) -> bool:
    """Jump to the end."""
    n: int = len(nums)
    jump: int = 0

    for i, num in enumerate(nums):
        if i <= jump:
            jump = max(jump, i + num)

    return jump >= n - 1


def tester(func: Callable[[list[int]], bool], nums: list[int], expected: bool) -> None:
    """Print custom output for testing."""
    if func(nums) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        nums_str, expected_str = line.strip().split()

        nums: list[int] = [int(x) for x in nums_str.split(",")]
        expected: bool = bool(int(expected_str))

        ans = jump_game(nums)

        print(f"Input: nums = {nums}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        tester(jump_game, nums, expected)
        print()
