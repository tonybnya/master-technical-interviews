from __future__ import annotations

from typing import Callable

from printer import print_fail, print_pass


def eval_RPN(tokens: list[str]) -> int:
    """Evaluate an expression in a Reverse Polish Notation."""
    stack: list[int] = []
    res: int = 0

    for c in tokens:
        if c == "*":
            res = int(stack.pop()) * int(stack.pop())
            stack.append(res)
        elif c == "/":
            a, b = int(stack.pop()), int(stack.pop())
            res = int(b / a)
            stack.append(res)
        elif c == "+":
            res = int(stack.pop()) + int(stack.pop())
            stack.append(res)
        elif c == "-":
            a, b = int(stack.pop()), int(stack.pop())
            res = b - a
            stack.append(res)
        else:
            stack.append(int(c))

    return stack[-1]


def tester(func: Callable[[list[str]], int], tokens: list[str], expected: int) -> None:
    """Print custom output for testing."""
    if func(tokens) == expected:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()

    for line in lines:
        tokens_str, expected_str = line.strip().split()

        tokens = tokens_str.split(",")
        expected = int(expected_str)

        ans = eval_RPN(tokens)

        print(f"Input: tokens = {tokens}")
        print(f"Expected Output: {expected}")
        print(f"My Answer: {ans}")
        tester(eval_RPN, tokens, expected)
        print()
