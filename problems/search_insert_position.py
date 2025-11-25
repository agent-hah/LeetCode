def search_insert(nums: list[int], target: int) -> int:
    MIN = nums[0]
    MAX = nums[-1]
    if (target <= MIN):
        return 0
    elif (target == MAX):
        return len(nums) - 1
    elif (target > MAX):
        return len(nums)
    l = 0
    r = len(nums) - 1
    while (l < r):
        m: int = l + (r - l) // 2
        val: int = nums[m]
        if val == target:
            return m
        elif target < val:
            r = m
        else:
            l = m + 1
    return l + 1 if nums[l] < target else l