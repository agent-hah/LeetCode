def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    intersection = set1.intersection(set2)
    return list(intersection)