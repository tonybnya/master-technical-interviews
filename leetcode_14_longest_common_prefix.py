from typing import Callable, List
from printer import print_fail, print_pass


def longestCommonPrefix(strs: List[str]) -> str:
    """Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    if not all(strs) or not strs:
        return ""

    strs: List[str] = sorted(strs)
    first: str = strs[0]
    last: str = strs[-1]
    lcp: str = ""

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return lcp
        lcp += first[i]

    return lcp


def tester(func: Callable[[List[str]], str], strs: List[str], res: str) -> None:
    """Print custom message for testing."""
    if func(strs) == res:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        strs, expected = line.strip().split()

        strs = [""] if strs == "0" else strs.split(",")
        if expected == "0":
            expected = ""

        print(f"Input: strs = {strs}")
        print(f'Expected Output: "{expected}"')
        print(f'My Answer: "{longestCommonPrefix(strs)}"')
        tester(longestCommonPrefix, strs, expected)
        print()
