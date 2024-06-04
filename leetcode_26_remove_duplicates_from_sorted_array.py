# pylint: disable=all

def remove_duplicates(nums):
    n = len(nums)
    i = 0
    j = 1

    while j < n:
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1

    return i + 1


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print(remove_duplicates(nums1))
    print(remove_duplicates(nums2))
