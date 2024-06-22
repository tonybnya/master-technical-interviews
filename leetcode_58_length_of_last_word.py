from typing import Callable

from printer import print_fail, print_pass


def lengthOfLastWord(s: str) -> int:
    """Given a string s consisting of words and spaces,
    return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.

    NB: A substring is contiguous non-empty sequence of characters within a string.
    """
    return len(s.split()[-1])


def tester(func: Callable[[str], int], s: str, output: int) -> None:
    """Printer function for testing."""
    if func(s) == output:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        s, expected_str = item.split(",")
        expected = int(expected_str)

        print(f'Input: s = "{s}"')
        print(f"Expected Ouput: {expected}")
        print(f"My Answer = {lengthOfLastWord(s)}")
        tester(lengthOfLastWord, s, expected)
        print()
