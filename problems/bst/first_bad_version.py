from typing import Callable

def firstBadVersion(n: int, func: Callable[[int], bool]) -> int:
    l = 0
    r = n

    while (l < r):
        m = l + (r - l) // 2

        if func(m):
            r = m
        else:
            l = m + 1
    return l


def isBadVersion(v: int) -> Callable[[int], bool]:
    def inner_function(x: int):
        return x >= v
    return inner_function


func = isBadVersion(3)

print(func(2))

print(firstBadVersion(5, func))