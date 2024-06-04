"""
Implementation of Binary Search Algorithm
"""
from typing import List


def search(arr: List[int], target: int) -> int:
    """
    Binary Search Algorithm
    """
    n: int = len(arr)
    lo: int = 0
    hi: int = n - 1

    while lo <= hi:
        mid: int = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1

    return -1
