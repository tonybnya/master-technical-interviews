"""
13. Roman to Integer
"""

from tests import print_fail, print_pass


def test_roman2int(func):
    """
    There are some test cases
    """
    cases = {
        "II": 2,
        "III": 3,
        "IV": 4,
        "IX": 9,
        "XII": 12,
        "XXVII": 27,
        "XXXIX": 39,
        "XL": 40,
        "LVIII": 58,
        "XC": 90,
        "CLX": 160,
        "CCVII": 207,
        "CCXLVI": 246,
        "CD": 400,
        "DCCLXXXIX": 789,
        "CM": 900,
        "MIX": 1009,
        "MLXVI": 1066,
        "MDCCLXXVI": 1776,
        "MCMXVIII": 1918,
        "MCMXLIV": 1944,
        "MCMXCIV": 1994,
        "MMXXIII": 2023,
        "MMCDXXI": 2421,
    }

    for key, value in cases.items():
        expected = f"Expected: {key} = {value}"
        output = f"Output: {key} = {func(key)}"

        if func(key) == value:
            print_pass(func.__name__)
        else:
            print_fail(func.__name__)

        print(expected)
        print(output)
        print("---")


# O(n) time
# O(1) space
def roman2int(roman):
    """Function to transform roman numerals to integers"""
    base = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    idx, integer = 0, 0

    while idx < len(roman):
        if idx + 1 < len(roman) and roman[idx : idx + 2] in base:
            integer += base[roman[idx : idx + 2]]
            idx += 2
        else:
            integer += base[roman[idx]]
            idx += 1

    return integer


if __name__ == "__main__":
    test_roman2int(roman2int)
