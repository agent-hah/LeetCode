def findTheDifference(s: str, t: str) -> str:
    res: int = 0
    for i  in range(len(s)):
        res ^= ord(s[i])
        res ^= ord(t[i])

    return chr(res ^ ord(t[-1]))


print(findTheDifference('ilovemen', 'imenslove'))