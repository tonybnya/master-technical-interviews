"""
Printer Functions for failing and passing tests.
"""
from typing import Callable


def print_fail(func: Callable) -> None:
    """
    Formatted string for failing
    """
    print(f"{func}\t failed! ❌")


def print_pass(func: Callable) -> None:
    """
    Formatted string for passing
    """
    print(f"{func}\t passed! ✅")
