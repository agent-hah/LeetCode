def findSubstring(s: str, words: list[str]) -> list[int]:
    res = []
    original_words = {}
    if (len(s) == 0 or len(words) == 0):
        return res
    length = len(words)
    for i in range(len(words)):
        original_words[words[i]] = original_words.get(words[i], 0) + 1
    

    for off_set in range(0, len(words[0])):
        start = off_set
        curr_words = {}
        count = 0
        for end in range(off_set + len(words[0]) - 1, len(s), len(words[0])):
            sub_string = s[end - len(words[0]) + 1: end + 1]
            if sub_string in original_words.keys():
                
                curr_words[sub_string] = curr_words.get(sub_string, 0) + 1
                count += 1

                while (curr_words.get(sub_string, 0) > original_words.get(sub_string, 0)):
                    removed_sub_string = s[start: start + len(words[0])]
                    curr_words[removed_sub_string] = curr_words.get(removed_sub_string, 0) - 1
                    start += len(words[0])
                    count -= 1
                
                if count == length:
                    res.append(start)

            else:
                count = 0
                curr_words.clear()
                start = end + 1
    return res

assert findSubstring("wellloveyous", ["well", "love", "yous"]) == [0]
assert findSubstring('', ["well"]) == []
assert findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
assert findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]) == [13]
assert findSubstring("foobarfoobar", ["foo", "bar"]) == [0, 3, 6]