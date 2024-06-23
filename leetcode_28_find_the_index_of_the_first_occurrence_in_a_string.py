from typing import Callable

from printer import print_fail, print_pass


def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i : i + len(needle)] == needle:
            return i

    return -1


def tester(
    func: Callable[[str, str], int], haystack: str, needle: str, res: int
) -> None:
    """Printer function for testing."""
    if func(haystack, needle) == res:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        haystack, needle, expected_str = item.split()
        expected: int = int(expected_str)

        print(f'Input: haystack = "{haystack}", needle = "{needle}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer = {strStr(haystack, needle)}")
        tester(strStr, haystack, needle, expected)
        print()
