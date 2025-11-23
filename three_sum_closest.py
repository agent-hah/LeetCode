def threeSumClosest(nums: list[int], target: int) -> int:
    res: int = 2 ** 31
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if abs(target - total) < abs(target - res):
                res = total
            
            if total < target:
                j += 1

                while (j < k and nums[j] == nums[j - 1]):
                    j += 1

            elif total > target:
                k -= 1

                while (j < k and nums[k] == nums[k + 1]):
                    k -=1

            else:
                return target
            
    return res


print(threeSumClosest([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -8))