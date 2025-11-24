def removeDuplicates(nums: list):
    ans = sorted(set(nums))
    k = len(ans)
    for i in range(k):
        nums.insert(i, ans.pop(0))
        nums.sort
    return k

nums = [1, 2, 3, 44, 5, 5, 1, 2, 5]
print(removeDuplicates(nums))
print(nums)

