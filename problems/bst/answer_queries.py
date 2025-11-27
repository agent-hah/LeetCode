def answerQueries(nums: list[int], queries: list[int]) -> list[int]:
    nums.sort()
    res = []

    for query in queries:
        ans = 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            

            val = sum(nums[:m])

            if val <= query:
                ans = m
                l = m + 1
            else:
                r = m - 1
        
        if sum(nums[:l]) <= query:
            ans = l
        
        res.append(ans)

    return res


print(answerQueries([4,5,2,1], [3,10,21]))