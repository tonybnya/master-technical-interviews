# pylint: disable=missing-docstring,redefining


def print_fail(func):
    print(f'{func}\t failed! ❌')


def print_pass(func):
    print(f'{func}\t Passed! ✅')


def test_two_sum(func, nums, target, output):
    if func(nums, target) == output:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


def two_sum(nums, target):
    hashmap = {}
    for index, element in enumerate(nums):
        difference = target - element
        if difference in hashmap:
            return [hashmap[difference], index]
        hashmap[element] = index
    return


def func(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        s = nums[i] + nums[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        return [i, j]

    return


if __name__ == '__main__':
    # tests = [
    #     {
    #         'nums': [2, 7, 11, 15],
    #         'output': [0, 1],
    #         'target': 9
    #     },
    #     {
    #         'nums': [3, 2, 4],
    #         'output': [1, 2],
    #         'target': 6
    #     },
    #     {
    #         'nums': [3, 3],
    #         'output': [0, 1],
    #         'target': 6
    #     }
    # ]

    # for i, test in enumerate(tests, start=1):
    #     print(f'Test #{i}')
    #     nums = test['nums']
    #     output = test['output']
    #     target = test['target']
    #     print(f'Input: nums = {nums}, target = {target}')
    #     print(f'Expected Output: {output}')
    #     print(f'My Answer: {func(nums, target)}')
    #     test_two_sum(func, nums, target, output)

    nums = list(map(int, input().strip().split()))
    print(f'### Test ###')
    output = [0, 1]
    target = 9
    print(f'Input: nums = {nums}, target = {target}')
    print(f'Expected Output: {output}')
    print(f'My Answer: {func(nums, target)}')
    test_two_sum(func, nums, target, output)