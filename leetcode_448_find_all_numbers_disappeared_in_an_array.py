# pylint: disable=all


def find_disappeared(nums):
    n = len(nums)
    s = set(nums)
    lst = []

    for i in range(1, n + 1):
        if i not in s:
            lst.append(i)

    return lst


if __name__ == '__main__':
    arr1 = [4, 3, 2, 7, 8, 2, 3, 1]
    arr2 = [1, 1]

    ans1 = find_disappeared(arr1)
    ans2 = find_disappeared(arr2)

    print(ans1)
    print(ans2)
