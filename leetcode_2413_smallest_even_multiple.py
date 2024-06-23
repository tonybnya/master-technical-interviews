from typing import Callable

from printer import print_fail, print_pass


def smallestEvenMultiple(n: int) -> int:
    """Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n."""
    return n if n % 2 == 0 else n * 2


def tester(func: Callable[[int], int], n: int, res: int) -> None:
    """Printer function for testing."""
    if func(n) == res:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        n_str, expected_str = item.split()
        n: int = int(n_str)
        expected: int = int(expected_str)

        print(f"Input: n = {n}")
        print(f"Expected Output: {expected}")
        print(f"My Answer = {smallestEvenMultiple(n)}")
        tester(smallestEvenMultiple, n, expected)
        print()
