"""
1672. Richest Customer Wealth
"""


def max_wealth(accounts):
    return max([sum(account) for account in accounts])
    # wealth = []

    # for account in accounts:
    #     wealth.append(sum(account))

    # return max(wealth)


if __name__ == '__main__':
    bank = [
        [[1, 2, 3], [3, 2, 1]],
        [[1, 5], [7, 3], [3, 5]],
        [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    ]

    for accounts in bank:
        print(max_wealth(accounts))
