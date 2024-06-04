"""
383. Ransom Note
"""


def can_construct(ransom_note, magazine):
    """
    Function to check if letters in magazine can be used
    to write ransom_note
    """
    map_a = {}
    map_b = {}

    for char in ransom_note:
        if char in map_a:
            map_a[char] += 1
        else:
            map_a[char] = 1

    for char in magazine:
        if char in map_b:
            map_b[char] += 1
        else:
            map_b[char] = 1

    ans = True
    for char in map_a:
        if char in map_b and (map_b[char] >= map_a[char]):
            ans = True
        else:
            ans = False
            return ans

    return ans
