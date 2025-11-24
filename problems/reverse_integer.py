def reverse(x):
    is_neg = x < 0
    string = str(abs(x))
    string = string[::-1]
    ans = int(string)
    ans = -ans if is_neg else ans
    if (ans > (2 ** 31) - 1) or (ans < - 2 ** 31):
        return 0
    else: return ans