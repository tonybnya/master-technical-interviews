# pylint: disable=all

def num_diff_int(word):
    # new = ''
    # for char in word:
    #     if not (ord(char) >= 48 and ord(char) <= 57):
    #         new += ' '
    #     else:
    #         new += char

    # chars = []

    # for char in new.split(' '):
    #     chars.append(char.lstrip('0'))

    # return len(set([char for char in chars if char != '']))
    ints = set()
    temp = ''

    for char in word:
        if ord(char) >= 48 and ord(char) <= 57:
            temp += char
        else:
            if temp:
                ints.add(int(temp))
            temp = ''

    if temp:
        ints.add(int(temp))

    return len(ints)


if __name__ == '__main__':
    tests = [
        {
            'word': 'a123bc34d8ef34',
            'output': 3
        },
        {
            'word': 'leet1234code234',
            'output': 2
        },
        {
            'word': 'a1b01c001',
            'output': 1
        }
    ]

    for i, test in enumerate(tests, start=1):
        word = test['word']
        output = test['output']
        answer = num_diff_int(word)

        print(f'Test #{i}')
        print(f'Input: word = "{word}"')
        print(f'Expected Output: {output}')
        print(f'My Answer: {answer}')
        print(type(answer))
        print(f'Test Passed? {output == answer}')
        print('---')
