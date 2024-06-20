from typing import Callable

from printer import print_fail, print_pass


def mySqrt(x: int) -> int:
    """Given a non-negative integer x, return the square root of x
    rounded down to the nearest integer.
    The returned integer should be non-negative as well.

    You must not use any built-in exponent function or operator.
    - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    """
    left: int = 1
    right: int = x

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
    # return int(x ** (1 / 2))


def tester(func: Callable[[int], int], input_: int, output: int) -> None:
    """Printer function for tests."""
    if func(input_) == output:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        x_str, expected_str = item.strip().split(" ")
        x, expected = int(x_str), int(expected_str)
        print(f'Input: x = "{x}"')
        print(f"Expected Output = {expected}")
        print(f"My Answer = {mySqrt(x)}")
        tester(mySqrt, x, expected)
        print()
