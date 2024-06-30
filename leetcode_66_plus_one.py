from typing import Callable, List
from printer import print_fail, print_pass


def plusOne(digits: List[int]) -> List[int]:
    """
    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer. The digits are
    ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """
    ans = int("".join(map(str, digits))) + 1
    return [int(c) for c in str(ans)]


def tester(
    func: Callable[[List[int]], List[int]], digits: List[int], expected: List[int]
) -> None:
    """Print custom output for testing."""
    if func(digits) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        digits_str, expected_str = line.strip().split()

        digits = [int(c) for c in digits_str.split(",")]
        expected = [int(c) for c in expected_str.split(",")]

        print(f"Input: digits = {digits}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {plusOne(digits)}")
        tester(plusOne, digits, expected)
        print()
