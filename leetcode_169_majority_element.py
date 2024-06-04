# pylint: disable=all


def majority(nums):
    nums.sort()
    n = len(nums)
    mid = n // 2

    return nums[mid]


if __name__ == '__main__':
    arr1 = [3, 2, 3]
    arr2 = [2, 2, 1, 1, 1, 2, 2]

    ans1 = majority(arr1)
    ans2 = majority(arr2)

    print(ans1)
    print(ans1 == 3)
    print('---')
    print(ans2)
    print(ans2 == 2)
