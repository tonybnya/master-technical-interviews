"""
1337. The K Weakest Rows in a Matrix
"""


def k_weakest_rows(mat, k):
    """Function to find the k weakest row in a matrix"""
    soldiers = {}
    rows = []

    for i, row in enumerate(mat):
        count = 0
        for item in row:
            if item == 1:
                count += 1
            soldiers[i] = count

    for key in soldiers:
        rows.append(key)

    rows.sort(key=lambda x: soldiers[x])
    print(rows[:k])


if __name__ == '__main__':
    mat1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    mat2 = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]

    tests = [
        {'k': 3, 'mat': mat1},
        {'k': 2, 'mat': mat2}
    ]

    for test in tests:
        k = test['k']
        mat = test['mat']
        k_weakest_rows(mat, k)
        print('---')
