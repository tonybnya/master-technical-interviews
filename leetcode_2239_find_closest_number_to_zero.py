from __future__ import annotations
from typing import Callable
from printer import print_fail, print_pass


def find_closest_number(nums: list[int]) -> int:
    """Find the closest number to zero."""
    closest: int = nums[0]

    for num in nums[1:]:
        if abs(num) < abs(closest):
            closest = num

    return abs(closest) if closest < 0 and abs(closest) in nums else closest


def tester(func: Callable[[list[int]], int], nums: list[int], expected: int) -> None:
    """Print custom output for testing."""
    if func(nums) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        nums_str, expected_str = line.strip().split()

        nums: list[int] = [int(n) for n in nums_str.split(",")]
        expected: int = int(expected_str)
        ans: int = find_closest_number(nums)

        print(f"Input: nums = {nums}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        tester(find_closest_number, nums, expected)
        print()
