from ordered_set import OrderedSet

def findMedianSortedArrays(l1, l2):
        all_nums = sorted(l1 + l2)
        length = len(all_nums)
        half = (len(all_nums) // 2)
        if (length % 2  == 1):
           median = all_nums[half // 2]
        else:
           median = (all_nums[half - 1] + all_nums[half]) / 2.0
        return median

print(findMedianSortedArrays([1,3], [2,4]))