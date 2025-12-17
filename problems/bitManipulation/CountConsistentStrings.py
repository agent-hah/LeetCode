def countConsistentStrings(allowed: str, words: list[str]) -> int:
    ref: set = set(allowed)
    res = 0
    for word in words:
        if ref.issuperset(set(word)):
            res += 1
    return res
