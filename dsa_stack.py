"""
Implementation of a Stack using a list.
"""

from typing import Iterable


class Stack:
    """Define a stack."""

    def __init__(self) -> None:
        """Initialize an empty list."""
        self.stack = []

    def is_empty(self) -> bool:
        """Check is the stack is empty or not."""
        return len(self.stack) == 0

    def push(self, n: int) -> None:
        """Add an element to the stack."""
        self.stack.append(n)

    def peek(self) -> int:
        """Get the last element added."""
        return self.stack[-1]

    def pop(self) -> int:
        """Remove and return the last element added."""
        return self.stack.pop()

    def length(self) -> int:
        """Get the length of the stack."""
        return len(self.stack)

    def print_stack(self) -> None:
        """Print the stack."""
        n: int = self.length()
        i: int = 0
        while i < n:
            print(f"|{self.stack[i]}|")
            i += 1
        print()


if __name__ == "__main__":
    s: Stack = Stack()
    rng: Iterable = range(10)

    for i in rng:
        s.push(i)

    s.print_stack()
