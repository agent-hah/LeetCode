def hasAlternatingBits(n: int) -> bool:
    if (n % 2 == 1):
        sawOne = False
    else:
        sawOne = True
    while n:
        if (n & 1) and sawOne:
            return False
        elif ((n & 1) == 0 and not sawOne):
            return False
        sawOne = not sawOne
        n >>= 1
    return True