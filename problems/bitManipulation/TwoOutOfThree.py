def twoOutOfThree(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    key: dict[int, int] = {}
    for num in set(nums1):
        key[num] = key.get(num, 0) + 1
    for num in set(nums2):
        key[num] = key.get(num, 0) + 1
    for num in set(nums3):
        key[num] = key.get(num, 0) + 1
    res = []
    for k, v in key.items():
        if v > 1:
            res.append(k)
    return res

print(twoOutOfThree([1, 1, 3, 2], [2, 3], [3]))