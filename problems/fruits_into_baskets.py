def numOfUnplacedFruits(fruits: list[int], baskets: list[int]) -> int:
    visited: list[bool] = [False for _ in range(len(baskets))]
    placed: dict[int, bool] = {i: False for i in range(len(fruits))}
    res = 0
    end = False

    for l in range(len(fruits)):
        r = 0
        while r < len(baskets):

            if (i for i in visited) == True:
                end = True
                break

            if not visited[r] and fruits[l] <= baskets[r]:
                placed[l] = True
                visited[r] = True
                break
            else:
                r += 1
        if end:
            break

    for i in range(len(placed)):
        if not placed[i]:
            res += 1
    return res

print(numOfUnplacedFruits([4,2,5], [3,5,4]))