# pylint: disable=all

def move_zeroes(nums):
    i = 0
    j = 0

    while i < len(nums):
        if nums[i] == 0:
            i += 1
        else:
            nums[j] = nums[i]
            i += 1
            j += 1

    while j < len(nums):
        nums[j] = 0
        j += 1

    return nums


if __name__ == '__main__':
    tests = [
        {
            'nums': [0, 1, 0, 3, 12],
            'output': [1, 3, 12, 0, 0]
        },
        {
            'nums': [0],
            'output': [0]
        }
    ]

    for i, test in enumerate(tests, start=1):
        nums = test['nums']
        output = test['output']
        answer = move_zeroes(nums)

        print(f'Input: nums = {nums}')
        print(f'Expected Output: {output}')
        print(f'My Answer: {answer}')
        print(f'Test Passed? {answer == output}')
        print('---')
