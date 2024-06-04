"""
412. Fizz Buzz
"""


def fizzbuzz(number):
    """FizzBuzz"""
    answer = [str(i) for i in range(1, number + 1)]

    for i, char in enumerate(answer):
        num = int(char)
        if num % 3 == 0 and num % 5 == 0:
            answer[i] = 'FizzBuzz'
        elif num % 3 == 0:
            answer[i] = 'Fizz'
        elif num % 5 == 0:
            answer[i] = 'Buzz'
        else:
            continue

    return answer


if __name__ == '__main__':
    number = 15
    print(fizzbuzz(number))
