
def removeElement(nums: list, val):
    ans = []
    if (len(nums) == 0):
        return 0
    for i in range(len(nums)):
        if (not (nums[i] == val)):
            ans.append(nums[i])
    k = len(ans)
    for i in range(k):
        nums.insert(i, ans.pop(0))
    return k

nums = [3, 2, 2, 3]

removeElement(nums, 3)
print(nums)