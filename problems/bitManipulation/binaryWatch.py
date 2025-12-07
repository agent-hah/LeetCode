def binaryWatch(turnedOn: int) -> list[str]:
    res: list[str] = []
    for h in range(12):
        for m in range(60):
            if bin(h).count("1") + bin(m).count("1") == turnedOn:
                if (m < 10):
                    res.append(str(h) + ":0" + str(m))
                else:
                    res.append(str(h) + ":" + str(m))
    return res

