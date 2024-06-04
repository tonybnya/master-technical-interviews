# pylint: disable=all

def cleaner(s):
    t = ''
    t = t.join(c.lower() for c in s if c.isalnum())

    return t


def is_palindrome(s):
    t = cleaner(s)

    if len(t) == 1:
        return True

    left = 0
    right = len(t) - 1

    while left <= right:
        if t[left] != t[right]:
            return False

        left += 1
        right -= 1

    return True
    # n = len(t)
    # mid = n // 2

    # for i in range(mid):
    #     if t[i] != t[n - 1 - i]:
    #         return False

    # return True


if __name__ == '__main__':
    chars = [
        'A man, a plan, a canal: Panama',
        'race a car',
        ' ',
        '0P',
        'a.',
        'a'
    ]

    for s in chars:
        print(is_palindrome(s))
