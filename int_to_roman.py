def intToRoman(num: int) -> str:
    ans: str = ""
    n: list[int] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    s: list[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    while (num > 0):
        if (num > n[i]):
            ans.join(s[i])
            num -= n[i]
        else:
            i += 1
    return ans