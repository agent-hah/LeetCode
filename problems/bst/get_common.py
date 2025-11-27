def getCommon(nums1: list[int], nums2: list[int]) -> int:
    nums1.sort()
    nums2.sort()

    for num in nums1:
        l = 0
        r = len(nums2) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums2[m] == num:
                return num
            elif nums2[m] > num:
                r = m - 1
            else:
                l = m + 1
    return -1

def getCommon2(nums1: list[int], nums2: list[int]) -> int:
    l,r = 0, 0
    while l < len(nums1) and r < len(nums2):
        if nums1[l] < nums2[r]:
            l+= 1
        elif nums1[l] > nums2[r]:
            r += 1   
        elif nums1[l] == nums2[r]:
            return nums1[l]
    return -1 