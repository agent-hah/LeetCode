def specialArray(nums: list[int]) -> int:
    nums.sort(reverse=True)
    for x in range(1, len(nums) + 1):
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2

            if nums[m] >= x:
                l = m + 1
            else:
                r = m
        if nums[l] >= x:
            l = l + 1
        if l == x: return l
    return -1


print(specialArray([0,4,3,0,4]))