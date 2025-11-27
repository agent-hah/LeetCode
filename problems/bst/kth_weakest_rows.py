def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    key : dict[int, int] = {}
    for i in range(len(mat)):
        l = 0
        r = len(mat[i]) - 1
        while l < r:
            if mat[i][r] == 1:
                key[i] = len(mat[i])
            m = l + (r - l) // 2

            if mat[i][m] == 1:
                l = m + 1
            else:
                r = m
        key[i] = l + 1 if mat[i][l] == 1 else l
    return sorted(key.keys(), key = lambda x: key.get(x, 0))[:k]


mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]

print(kWeakestRows(mat, 3))