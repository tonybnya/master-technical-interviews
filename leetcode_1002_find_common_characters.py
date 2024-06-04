# pylint: disable=all
from collections import Counter


def commonChars(words):
    if not words:
        return

    res = []

    # for ch in words[0]:
    #     checker[ch] = checker.get(ch, 0) + 1
    checker = Counter(words[0])

    for word in words[1:]:
        checker &= Counter(word)

    for ch, count in checker.items():
        res.extend([ch] * count)

    return res


if __name__ == "__main__":
    tests = [
        {"words": ["bella", "label", "roller"], "output": ["e", "l", "l"]},
        {"words": ["cool", "lock", "cook"], "output": ["c", "o"]},
    ]

    for i, test in enumerate(tests, start=1):
        words = test["words"]
        output = test["output"]
        answer = commonChars(words)

        print(f"Test #{i}")
        print(f"Input: words = {words}")
        print(f"Expected: {output}")
        print(f"Got: {answer}")
        print(f"Tested Passed? {output == answer}")
        print("---")
