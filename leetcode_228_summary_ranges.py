from __future__ import annotations
from typing import Callable
from printer import print_fail, print_pass


def summary_ranges(nums: list[int]) -> list[str]:
    """Return the smallest sorted list of ranges that cover all the numbers in the array exactly."""
    n: int = len(nums)

    if n == 0:
        return []

    ranges: list[str] = []
    i: int = 0

    while i < n:
        start: int = nums[i]

        while i + 1 < n and nums[i + 1] == nums[i] + 1:
            i += 1
        end = nums[i]

        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{end}")

        i += 1

    return ranges


def tester(
    func: Callable[[list[int]], list[str]], nums: list[int], expected: list[str]
) -> None:
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
        expected: list[str] = [n for n in expected_str.split(",")]

        ans = summary_ranges(nums)

        print(f"Input: nums = {nums}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        tester(summary_ranges, nums, expected)
        print()
