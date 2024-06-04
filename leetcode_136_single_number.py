# pylint: disable=all


def single(nums):
    xor = 0

    for num in nums:
        xor ^= num

    return xor


if __name__ == '__main__':
    arr1 = [2, 2, 1]
    arr2 = [4, 1, 2, 1, 2]
    arr3 = [1]

    ans1 = single(arr1)
    ans2 = single(arr2)
    ans3 = single(arr3)

    print(ans1)
    print(ans2)
    print(ans3)
