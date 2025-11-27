def countBits(n: int) -> list[int]:
    res = []
    for i in range(n + 1):
        dist = 0
        binary = bin(i)[2::]
        res.append(binary.count("1"))
    return res