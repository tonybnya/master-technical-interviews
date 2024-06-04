# pylint: disable=all

def max_profit(prices):
    i = 0
    j = 1
    profit = 0

    while j < len(prices):
        sub = prices[j] - prices[i]

        if prices[i] < prices[j]:
            profit = max(profit, sub)
        else:
            i = j
        j += 1

    return profit


if __name__ == '__main__':
    tests = [
        {
            'prices': [7, 1, 5, 3, 6, 4],
            'output': 5
        },
        {
            'prices': [7, 6, 4, 3, 1],
            'output': 0
        },
        {
            'prices': [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9],
            'output': 9
        },
        {
            'prices': [1],
            'output': 0
        }
    ]

    for i, test in enumerate(tests, start=1):
        prices = test['prices']
        output = test['output']
        answer = max_profit(prices)

        print(f'Test #{i}')
        print(f'prices = {prices}')
        print(f'Expected Output: {output}')
        print(f'Answer: {answer}')
        print(answer == output)
        print('---')
