def countPairs(nums: list[int], target: int) -> int:

    nums.sort()

    res : set[tuple[int, int]] = set()

    for i in range(len(nums)):
        j = i + 1

        while j < len(nums):

            if nums[i] + nums[j] < target:
                res.add((i, j))
                j += 1
            else:
                break

    return len(res)

print(countPairs([-1,1,2,3,1], 2))
print(countPairs([-6,2,5,-2,-7,-1,3], -2))

def countPairs1(nums: list[int], target: int) -> int:
    nums.sort()
    left=0
    right=len(nums)-1
    res=0
    while(left<right):
        if(nums[left]+nums[right]<target):
            res+=right-left
            left+=1
        else:
            right-=1
    return res

print(countPairs1([-1,1,2,3,1], 2))
print(countPairs1([-6,2,5,-2,-7,-1,3], -2))