"""
Leetcode 1: Two Sum
"""
from typing import List, Union
from binary_search import search


def helper(arr: List[int], target: int) -> List[int]:
    """
    Helper Function to iterate and binary search.
    runtime: O(nlogn)
    extra memory space: O(1)
    """
    pair: List[int]
    i: int = 0
    while i < len(arr):  # O(n)
        diff = target - arr[i]
        j = search(arr, diff)  # O(logn)
        if j == -1:
            i += 1
        else:
            pair = [arr[i], arr[j]]
            return pair

    return [-1, -1]


def two_sum(arr: List[int], target: int) -> Union[List[int], str]:
    """
    Given an array of integers, find a pair that sum is target.
    Then their index positions as array.

    :param arr: list of integers
    :param target: integer
    :return: a list of indexes
    """
    n: int = len(arr)

    # Solution 1: Naive/Brute Force approach
    # runtime: O(n^2)
    # extra memory space: O(1)
    # for i, num in enumerate(arr):  # O(n)
    #     for j in range(i + 1, n):  # O(n)
    #         if num + arr[j] == target:
    #             return [i, j]

    # return "No Two Sum Solution"

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if arr[j] == target - arr[i]:
    #             return [i, j]

    # return "No Two Sum Solution"

    # Solution 2: Sorting approach
    # runtime: O(nlogn)
    # extra memory space: O(n)
    # ans: List[int] = []
    # lst: List[int] = sorted(arr)  # runtime: O(nlogn) - extra memory space: O(n)
    # pair: List[int] = helper(lst, target)

    # if -1 in pair:
    #     return "No Two Sum Solution"

    # # runtime: O(n)
    # for i, num in enumerate(arr):
    #     if num == pair[0] or num == pair[1]:
    #         ans.append(i)

    # return ans

    # Solution 3: Optimal
    # runtime: O(n)
    # extra memory space: O(n)
    hashmap = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return "No Two Sum Solution"


if __name__ == "__main__":
    pass
