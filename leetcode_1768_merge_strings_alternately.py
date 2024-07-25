from __future__ import annotations
from typing import Callable
from printer import print_fail, print_pass


def merge_strings_alternately(word1: str, word2: str) -> str:
    """Merge Strings Alternately."""
    m: int = len(word1)
    n: int = len(word2)
    merged = [""] * (m + n)

    i: int = 0
    j: int = 0
    k: int = 0
    while i < m and j < n and k < m + n:
        merged[k] = word1[i]
        merged[k + 1] = word2[j]
        i += 1
        j += 1
        k += 2

    if i != m:
        while i < m and j < m + n:
            merged[k] = word1[i]
            i += 1
            k += 1
    elif j != n:
        while j < n and k < m + n:
            merged[k] = word2[j]
            j += 1
            k += 1

    return "".join(merged)


def tester(
    func: Callable[[str, str], str], word1: str, word2: str, expected: str
) -> None:
    """Print custom output for testing."""
    if func(word1, word2) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        words, expected = line.strip().split()

        word1, word2 = words.split(",")
        ans: str = merge_strings_alternately(word1, word2)

        print(f"Input: word1 = {word1}, word2 = {word2}")
        print(f"Expected Ouput: {expected}")
        print(f"My Answer: {ans}")
        tester(merge_strings_alternately, word1, word2, expected)
        print()
