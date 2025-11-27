import bisect

def maximumCount(nums: list[int]) -> int:
    total_neg = 0
    total_pos = 0

    comparision = []

    for i in nums:
        if i != 0:
           comparision.append(i)

    if len(comparision) == 0:
        return 0

    l = 0
    r = len(comparision) - 1

    while l < r:
        m = l + (r - l) // 2

        if comparision[m] > 0:
            total_pos = len(comparision) - m
            r = m - 1
        elif comparision[m] < 0:
            total_neg = m + 1
            l = m + 1

    return max(total_pos, total_neg)


print(maximumCount([-2,-1,-1,1,2,3]))
print(maximumCount([-3,-2,-1,0,0,1,2]))

def maximumCount2(nums: list[int]) -> int:
    total_pos = bisect.bisect_left(nums, 0)
    total_neg = len(nums) - bisect.bisect_right(nums, 0)
    return max(total_neg, total_pos)


print(maximumCount2([-2,-1,-1,1,2,3]))
print(maximumCount2([-3,-2,-1,0,0,1,2]))
