from typing import Callable

from printer import print_fail, print_pass


def isValid(word: str) -> bool:
    """A word is considered valid if:

    - It contains a minimum of 3 characters.
    - It contains only digits (0-9), and English letters (uppercase and lowercase).
    - It includes at least one vowel.
    - It includes at least one consonant.

    You are given a string word.
    Return true if word is valid, otherwise, return false.
    """
    vowels: str = "aeiou"
    vowels += vowels.upper()

    consonants: str = "bcdfghjklmnpqrstvwxyz"
    consonants += consonants.upper()

    digits = "".join(str(i) for i in range(10))

    if len(word) < 3:
        return False

    has_vowel: bool = False
    has_consonant: bool = False

    for char in word:
        if char in vowels:
            has_vowel = True

        if char in consonants:
            has_consonant = True

        if char not in vowels + consonants + digits:
            return False

    return has_vowel and has_consonant


def tester(func: Callable[[str], bool], word: str, output: int) -> None:
    """Printer function for tests."""
    if func(word) == output:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    for item in data:
        word, expected_str = item.strip().split(" ")
        expected = bool(int(expected_str))

        print(f'Input: word ="{word}"')
        print(f"Expected Output: {expected}")
        print(f"My Answer = {isValid(word)}")
        tester(isValid, word, expected)
        print()
