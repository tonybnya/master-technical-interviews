# pylint: disable=all


def bs(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def test_bs(func, nums, target, output):
    if func(nums, target) == output:
        print(f'{func.__name__} Test Passed! ✅')
    else:
        print(f'{func.__name__} Test Failed! ❌')


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]

    target1 = 9
    target2 = 2

    output1 = 4
    output2 = -1

    ans1 = bs(nums, target1)
    ans2 = bs(nums, target2)

    print(f'Input: nums = {nums}, target = {target1}')
    print(f'Expected Output: {output1}')
    print(f'My Answer: {ans1}')
    test_bs(bs, nums, target1, output1)
    print('---')
    print(f'Input: nums = {nums}, target = {target2}')
    print(f'Expected Output: {output2}')
    print(f'My Answer: {ans2}')
    test_bs(bs, nums, target2, output2)
