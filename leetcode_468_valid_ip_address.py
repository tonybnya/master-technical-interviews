# pylint: disable=all


def splitter(string, sep):
    return string.split(sep)


def func4(queryIP):
    for char in queryIP:
        if ord(char) != 46 and not (48 <= ord(char) and 57 >= ord(char)):
            return False

    # chars = queryIP.split('.')
    chars = splitter(queryIP, '.')

    if len(chars) != 4:
        return False

    for char in chars:
        if not char:
            return False

        if len(char) == 1 and char == '0':
            continue

        if len(char) > 0 and char.startswith('0'):
            return False

        num = int(char)

        if not (0 <= num and 255 >= num):
            return False

    return True


def func6(queryIP):
    for char in queryIP:
        if ord(char) != 58 \
                and not (48 <= ord(char) and 57 >= ord(char)) \
                and not (65 <= ord(char) and 70 >= ord(char)) \
                and not (97 <= ord(char) and 102 >= ord(char)):
            return False

    chars = splitter(queryIP, ':')

    if len(chars) != 8:
        return False

    for char in chars:
        if not (1 <= len(char) and 4 >= len(char)):
            return False

    return True


def validIP(queryIP):
    answer = ''

    if func4(queryIP):
        answer = 'IPv4'
    elif func6(queryIP):
        answer = 'IPv6'
    else:
        answer = 'Neither'

    return answer


if __name__ == '__main__':
    tests = [
        {
            'queryIP': '172.16.254.1',
            'output': 'IPv4'
        },
        {
            'queryIP': '2001:0db8:85a3:0:0:8A2E:0370:7334',
            'output': 'IPv6'
        },
        {
            'queryIP': '256.256.256.256',
            'output': 'Neither'
        },
        {
            'queryIP': '192.168.1.1',
            'output': 'IPv4'
        },
        {
            'queryIP': '192.168.1.0',
            'output': 'IPv4'
        },
        {
            'queryIP': '192.168.01.1',
            'output': 'Neither'
        },
        {
            'queryIP': '192.168.1.00',
            'output': 'Neither'
        },
        {
            'queryIP': '192.168@1.1',
            'output': 'Neither'
        },
        {
            'queryIP': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
            'output': 'IPv6'
        },
        {
            'queryIP': '2001:db8:85a3:0:0:8A2E:0370:7334',
            'output': 'IPv6'
        },
        {
            'queryIP': '2001:0db8:85a3::8A2E:037j:7334',
            'output': 'Neither'
        },
        {
            'queryIP': '02001:0db8:85a3:0000:0000:8a2e:0370:7334',
            'output': 'Neither'
        },
        {
            'queryIP': '1.0.1.',
            'output': 'Neither'
        }
    ]

    for i, test in enumerate(tests, start=1):
        queryIP = test['queryIP']
        output = test['output']
        answer = validIP(queryIP)

        check = answer == output
        if check:
            check = '✅'
        else:
            check = '❌'

        print(f'Test #{i}')
        print(f'Input: queryIP = {queryIP}')
        print(f'Expected Output: {output}')
        print(f'My answer: {answer}')
        print(f'Test Passed ? {check}')
        print('---')
