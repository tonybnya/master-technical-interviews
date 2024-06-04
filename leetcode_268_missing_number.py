# pylint: disable=all


def missing_number(nums):
    n = len(nums)
    # miss = 0

    # for num in nums:
    #     diff = n - num
    #     miss = max(miss, diff)

    # if miss == n:
    #     miss -= 1

    # return miss

    # hashmap = {}

    # for i, num in enumerate(nums):
    #     hashmap[num] = i

    # for i in range(n+1):
    #     if i not in hashmap:
    #         return i
    total = sum(nums)
    s = sum(range(n + 1))

    return s - total


if __name__ == '__main__':
    arr1 = [3, 0, 1]
    arr2 = [0, 1]
    arr3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    ans1 = missing_number(arr1)
    ans2 = missing_number(arr2)
    ans3 = missing_number(arr3)

    print(ans1)
    print(ans2)
    print(ans3)
