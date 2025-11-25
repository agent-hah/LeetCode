# The index represents the number that should be there

def missingNumber(nums: list[int]) -> int:
    l: int = 0
    r: int = len(nums)

    nums.sort()

    while (l < r):
        m = l + (r - l) // 2
        val = nums[m]
        if val > m:
            r = m
        else:
            l = m + 1

    return l

# Or if you want to be lazy
def missingNumber2(nums: list[int]):
    return sum(range(len(nums)+1)) - sum(nums)


print(missingNumber([0, 1, 2]))
print(missingNumber2([0, 2, 3]))