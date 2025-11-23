def myAtoi(s: str) -> int:
    ans = 0
    for i in range(len(s)):
        if s[i] == "-" or s[i] == "+" or s[i].isdigit():
            if s[i] == '-':
                ans = - get_num(s[i+1:])
                break
            elif s[i] == "+":
                ans = get_num(s[i+1:])
                break
            else: 
                ans = get_num(s[i:]) 
                break
    if ans > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif ans < - 2 ** 31:
        return -2 ** 31
    else: return ans
            
            

def get_num(s: str) -> int:
    ans = ""
    for i in range(len(s)):
        if s[i] == "-" or s[i] == "+":
            break
        if not s[i].isdigit():
            break
        ans += s[i]
    return int(ans)

print(myAtoi('42'))
print(myAtoi("     -052"))
print(myAtoi("words and 987"))