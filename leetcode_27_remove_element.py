# pylint: disable=all


def func(nums, val):
    hashmap = {}
    k = 0

    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1

    for key in hashmap:
        if key != val:
            k += hashmap[key]

    return k, nums


def switch(a, b):
    temp = a
    a = b
    b = temp


def func1(nums, val):
    count_val = 0

    for num in nums:
        if num == val:
            count_val += 1

    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] == val and nums[j] != val:
            switch(nums[i], nums[j])
            i += 1
            j -= 1
        elif nums[i] != val and nums[j] == val:
            j -= 1
        else:
            j -= 1
            switch(nums[i], nums[j])
            i += 1
            j -= 1

    nums = nums[:-count_val]
    k = len(nums)

    return k, nums


def remove_element(nums, val):
    idx = 0

    for num in nums:
        if num != val:
            nums[idx] = num
            idx += 1

    return idx, nums[:idx]


if __name__ == '__main__':
    tests = [
        {
            'input': {
                'nums': [3, 2, 2, 3],
                'val': 3
            },
            'output': {
                'k': 2,
                'arr': [2, 2]
            }
        },
        {
            'input': {
                'nums': [0, 1, 2, 2, 3, 0, 4, 2],
                'val': 2
            },
            'output': {
                'k': 5,
                'arr': [0, 1, 4, 0, 3]
            }
        }
    ]

    for i, test in enumerate(tests, start=1):
        nums = test['input']['nums']
        val = test['input']['val']
        k = test['output']['k']
        arr = test['output']['arr']
        myk, myarr = remove_element(nums, val)

        print(f'Test #{i}:')
        print(f'Input: nums = {nums}, val = {val}')
        print(f'Expected Output: k = {k}, nums = {arr}')
        print(f'My Answer: k = {myk}, nums = {myarr}')
        print(k == myk)
        print(arr == myarr)
        print('---')
