def lengthOfLongestSubstring(s):
        prev = {}
        maxlen = 0
        total = 0
        left = 0
        for right in range(len(s)):
            if (not s[right] in prev or prev[s[right]] < left):
                total += 1
                maxlen = max(maxlen, right - left + 1)
                prev[s[right]] = right
            else:
                left = prev[s[right]] + 1
                prev[s[right]] = right
        return maxlen

print(lengthOfLongestSubstring("abcabcbb"))
     