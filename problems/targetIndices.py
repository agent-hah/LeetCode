def targetIndices(nums: list[int], target: int) -> list[int]:
    res = set()
    l = 0
    r = len(nums) - 1
    nums.sort()

    while l <= r:
        m = l + (r - l) // 2

        val = nums[m]

        if val == target:
            check_left, check_right = m - 1, m + 1
            while check_left >= 0 and nums[check_left] == val:
                res.add(check_left)
                check_left -= 1
            while check_right < len(nums) and nums[check_right] == val:
                res.add(check_right)
                check_right += 1
            res.add(m)
            break
        elif val > target:
            r = m - 1
        elif val < target:
            l = m + 1
    return sorted(res)


# [0, 1, 1, 2, 4]
# ans should be [1, 2]
print(targetIndices([0, 2, 4, 1 , 1], 1))
print(targetIndices([100,1,100], 100))