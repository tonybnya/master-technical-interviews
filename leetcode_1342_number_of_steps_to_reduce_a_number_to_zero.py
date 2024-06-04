"""
1342. Number of Steps to Reduce a Number to Zero
"""


def steps(num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num -= 1
            count += 1

    return count


if __name__ == '__main__':
    nums = [14, 8, 123]

    for num in nums:
        print(steps(num))
