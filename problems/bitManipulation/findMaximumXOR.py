def findMaximumXOR(nums: list[int]) -> int:   
    maxInt: int = 0 
    for num in nums:
        complement = abs(~num)
        if complement in nums:
            maxInt = max(complement, maxInt)
    return maxInt

# 5:  000011
# 25: 010101