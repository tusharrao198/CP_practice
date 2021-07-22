class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = []
        dd = {}
        for i in s:
            dd[i] = dd.get(i, 0) + 1

        for k, v in dd.items():
            if v == 1:
                lst.append(k)
        for i in range(len(s)):
            if s[i] in lst:
                return i
        return -1


# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/