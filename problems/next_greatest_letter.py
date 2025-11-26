def nextGreatestLetter(letters: list[str], target: str) -> str:
    if (letters[0] > target or letters[-1] < target):
        return letters[0]
    
    l = 0
    r = len(letters) - 1

    ans = ""
    while (l <= r):
        m = l + (r - l) // 2

        if letters[m] > target:
            ans = letters[m]
            r = m - 1
        else:
            l = m + 1
    return ans if ans != "" else letters[0]
        
assert nextGreatestLetter(["a", "b", "c"], "a") == "b"

