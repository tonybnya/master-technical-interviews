from typing import Callable
from printer import print_fail, print_pass


def isSubsequence(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from
    the original string by deleting some (can be none) of the
    characters without disturbing the relative positions of the
    remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    sptr, tptr = 0, 0

    while sptr < len(s) and tptr < len(t):
        if s[sptr] == t[tptr]:
            sptr += 1
        tptr += 1

    return sptr == len(s)
    # if len(s) > len(t):
    #     return False

    # i, ans = 0, ""

    # for i in range(len(t)):
    #     c: str = t[i]
    #     if c in s:
    #         ans += c

    # return ans == s


def tester(func: Callable[[str, str], bool], s: str, t: str, res: str) -> None:
    """Print custom message for testing."""
    if func(s, t) == res:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        strs, expected_str = line.strip().split(",")

        s, t = strs.split()
        expected = bool(int(expected_str))

        print(f'Input: s = "{s}", t = "{t}"')
        print(f'Expected Output: "{expected}"')
        print(f'My Answer: "{isSubsequence(s, t)}"')
        tester(isSubsequence, s, t, expected)
        print()
