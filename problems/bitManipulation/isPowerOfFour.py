def isPowerOfFour(n: int) -> bool:
    return (n > 0) and (n & (n-1) == 0) and (bin(n - 1)[2::].count("1") % 2 == 0)

print(isPowerOfFour(4 ** 1000000000))