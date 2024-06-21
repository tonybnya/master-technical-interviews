from typing import Callable, List

from printer import print_fail, print_pass


def runningSum(nums: List[int]) -> List[int]:
    """Given an array nums.
    We define a running sum of an array as
    runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    """
    s, rs = 0, []

    for num in nums:
        s += num
        rs.append(s)

    return rs


def tester(
    func: Callable[[List[int]], List[int]], nums: List[int], output: List[int]
) -> None:
    """Printer function for testing."""
    if func(nums) == output:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        x, y = item.strip().split(" ")

        nums: List[int] = [int(char) for char in x.split(",")]
        expected: List[int] = [int(char) for char in y.split(",")]

        print(f"Input: nums = {nums}")
        print(f"Expected Output: {expected}")
        print(f"My Answer = {runningSum(nums)}")
        tester(runningSum, nums, expected)
        print()
