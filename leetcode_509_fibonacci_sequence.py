# pylint: disable=all

from typing import Dict, Union


def fib_memo(n: int, cache: Dict = {}) -> int:
    """Helper function using memoization."""
    if n < 0 or not isinstance(n, int):
        return -1

    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    return cache[n]

def fibonacci(n: int) -> int:
    """Calculate Fibonacci sequence of n."""
    return fib_memo(n)
