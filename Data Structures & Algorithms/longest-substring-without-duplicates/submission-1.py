class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        a = 0

        for c in s:
            if c not in temp:
                temp += c
            else:
                a = max(a, len(temp))
                temp = temp[temp.index(c) + 1:]
                temp += c

        return max(a, len(temp))
        