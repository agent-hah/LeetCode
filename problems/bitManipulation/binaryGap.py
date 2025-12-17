def binaryGap(n: int) -> int:
    s = bin(n)[2::]
    if (s.count("1") == 1):
        return 0
    temp = 1
    res = 0
    s = list(s)
    s.pop(0)
    while s:
        if s.pop(0) == "1":
            res = max(res, temp)
            temp = 1
        else:
            temp += 1
    return res


def binaryGap2(n: int) -> int:
    s = bin(n)[2::]
    prev = -1
    res = 0
    for i, bit in enumerate(s):
        if bit == "1":
            if prev != -1:
                res = max(res, i - prev)
            prev = i
    return res



print(binaryGap(13))
print(binaryGap2(13))
x = 0
x &= 1
print(x)