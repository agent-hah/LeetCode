def countNegatives(grid: list[list[int]]) -> int:
        res = 0
        for row in grid:
            l = 0
            r = len(row) - 1
            if row[l] < 0:
                res += len(row)
                continue

            if row[r] >= 0:
                continue

            while l < r:
                m = l + (r - l) // 2

                if row[m] < 0:
                    r = m
                else: 
                    l = m + 1
            res += (len(row) - r)

        return res

print(countNegatives([[3,2],[1,0]]))