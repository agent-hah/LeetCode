def isPowerOfFour(n: int) -> bool:
    # 4 = 100
    # 1 = 001
    # 16 = 10000
    # 64 = 1000000
    # 6 = 110
    return (n > 0) and (n & (n-1) == 0) and (bin(n - 1)[2::].count("1") % 2 == 0)

print(isPowerOfFour(4 ** 1000000000))