from printer import print_fail, print_pass
from typing import Callable


def first_letter_to_appear_twice(s: str) -> str:
    """Given a string s consisting of lowercase English letters,
    return the first letter to appear twice.
    """
    hm: dict = {}

    for char in s:
        hm[char] = hm.get(char, 0) + 1
        if hm[char] == 2:
            return char

    # l = []
    # for char in s:
    #     if char in l:
    #         return char
    #     l.append(char)


def tester(func: Callable[[str], str], input_: str, output: str) -> None:
    """Printer function for tests."""
    if func(input_) == output:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        s, expected = item.strip().split(" ")
        print(f'Input: s = "{s}"')
        print(f'Expected Output = "{expected}"')
        print(f'My Answer = "{first_letter_to_appear_twice(s)}"')
        tester(first_letter_to_appear_twice, s, expected)
        print()
