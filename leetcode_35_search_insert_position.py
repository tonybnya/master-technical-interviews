# pylint: disable=all


def search_insert_position(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l


if __name__ == '__main__':
    nums1 = [1, 3, 5, 6]
    nums2 = [3, 6, 7, 8, 10]
    nums3 = [1, 5, 6, 8, 9, 10]

    target1 = 5
    target2 = 2
    target3 = 7
    target4 = 0
    target5 = 4
    target6 = 1

    ans1 = search_insert_position(nums1, target1)
    ans2 = search_insert_position(nums1, target2)
    ans3 = search_insert_position(nums1, target3)
    ans4 = search_insert_position(nums1, target4)
    ans5 = search_insert_position(nums1, target5)
    ans6 = search_insert_position(nums2, target5)
    ans7 = search_insert_position(nums3, target6)

    print(ans1)
    print(ans1 == 2)
    print('---')
    print(ans2)
    print(ans2 == 1)
    print('---')
    print(ans3)
    print(ans3 == 4)
    print('---')
    print(ans4)
    print(ans4 == 0)
    print('---')
    print(ans5)
    print(ans5 == 2)
    print('---')
    print(ans6)
    print(ans6 == 1)
    print('---')
    print(ans7)
    print(ans7 == 0)
