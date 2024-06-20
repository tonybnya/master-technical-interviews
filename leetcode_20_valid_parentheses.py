from collections import deque
from typing import Callable

from printer import print_fail, print_pass


def isValid(s: str) -> bool:
    """Given a string s containing just the characters
    '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    """
    hm: dict = {"}": "{", "]": "[", ")": "("}
    stack: deque = deque()

    for char in s:
        if char not in hm:
            stack.append(char)
        elif not stack or stack.pop() != hm[char]:
            return False

    return not stack


def tester(func: Callable[[str], bool], input_: str, output: bool) -> None:
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
        expected_bool = bool(int(expected))
        print(f'Input: s = "{s}"')
        print(f"Expected Output = {expected_bool}")
        print(f"My Answer = {isValid(s)}")
        tester(isValid, s, expected_bool)
        print()
