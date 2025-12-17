def countPrimeSetBits(left: int, right: int) -> int:
    res = 0
    for num in range(left, right + 1):
        res += 1 if isPrime(bin(num).count("1")) else 0
    return res

def isPrime(num: int) -> bool:
    if (num == 1):
        return False
    div = 2
    while (div ** 2 <= num):
        if num % div == 0:
            return False
        div += 1
    return True


print(countPrimeSetBits(6, 10))

# 6 110