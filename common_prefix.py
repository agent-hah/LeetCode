def longestCommonPrefix(strs: list[str]) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        while (prefix != strs[i][:len(prefix)]):
            prefix = prefix[:-1]
            if len(prefix) == 0:
                break
    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))