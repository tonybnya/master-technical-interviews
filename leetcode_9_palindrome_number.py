from typing import Callable
from printer import print_fail, print_pass


def isPalindrome(x: int) -> bool:
    """
    Given an integer x, return true if x is a  palindrome, and false otherwise.
    """
    x_str: str = str(x)

    i: int = 0
    j: int = len(x_str) - 1

    while i <= j:
        if x_str[i] != x_str[j]:
            return False
        i += 1
        j -= 1

    return True


def tester(func: Callable[[int], bool], x: int, expected: bool) -> None:
    """Print custom output for testing."""
    if func(x) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        x_str, expected_str = line.strip().split()

        x = int(x_str)
        expected = bool(int(expected_str))

        print(f"Input: x = {x}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {isPalindrome(x)}")
        tester(isPalindrome, x, expected)
        print()
