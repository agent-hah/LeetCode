from functools import reduce
from operator import or_

def subsetXORSum(nums: list[int]) -> int:
        return reduce(or_, nums)<<(len(nums)-1)
        res = 0
        for mask in range(0, 1 << len(nums)):
            sub = 0
            i = 0
            while mask:
                if (mask & 1):
                    sub ^= nums[i]
                mask >>= 1
                i += 1
            res += sub
        return res


print(subsetXORSum([1, 3]))