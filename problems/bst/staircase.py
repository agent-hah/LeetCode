import math

def arrangeCoins(n: int) -> int:
    l = 1
    r = (n // 2) + 1

    while (l < r):
        m = l + (r - l) // 2

        if (m * (m + 1) / 2) >= n:
            r = m
        else:
            l = m + 1
    return l if (l * (l + 1) / 2) <= n else l - 1

assert arrangeCoins(2) == 1
assert arrangeCoins(3) == 2