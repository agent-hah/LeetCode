def toHex(num: int) -> str:
    if num == 0:
        return "0"
    if num < 0:
        num += 2**32
    h = "0123456789abcdef"
    r = []
    while num:
        r.append(h[num & 15])
        num >>= 4
    return "".join(r[::-1])

print(toHex(26))