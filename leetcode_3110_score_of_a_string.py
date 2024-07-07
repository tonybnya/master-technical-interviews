from typing import Callable
from printer import print_fail, print_pass


def scoreOfString(s: str) -> int:
    """Score a string."""
    n: int = len(s)
    score: int = 0

    if n == 0:
        score = 0
    elif n == 1:
        score = ord(s[0])
    else:
        for i in range(n - 1):
            val: int = ord(s[i]) - ord(s[i + 1])

            val = (-1 * val) if val < 0 else val

            score += val

    return score


def tester(func: Callable[[str], int], s: str, expected: int) -> None:
    """Print custom output for testing."""
    if func(s) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        s, expected_str = line.strip().split()
        expected = int(expected_str)

        print(f'Input: s = "{s}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer: {scoreOfString(s)}")
        tester(scoreOfString, s, expected)
        print()
