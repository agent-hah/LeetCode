def kthSmallest(matrix: list[list[int]], k: int) -> int:
    total = []
    for row in matrix:
        for ele in row:
            total.append(ele)

    total.sort()
    return total[k-1]


print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
print(kthSmallest([[1,2],[1,3]], 2))