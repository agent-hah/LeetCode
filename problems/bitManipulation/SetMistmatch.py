def findErrorNums(nums: list[int]) -> list[int]:
    myMap: dict[int, bool] = {i: False for i in range(1, len(nums) + 1)}
    res: list[int] = [0, 0]
    for num in nums:
        if myMap.get(num, False):
            res[0] = num
        else:
            myMap[num] = True
    for (k, v) in myMap.items():
        if not v:
            res[1] = k
    return res

print(findErrorNums([1, 2, 2, 4]))
print(findErrorNums([5,3,6,1,5,4,7,8]))
nums = [i for i in range(2, 101)]
nums.insert(49, 69)
print(findErrorNums(nums))