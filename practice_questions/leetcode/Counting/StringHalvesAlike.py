class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]

        counta, countb = 0, 0
        for i in range(len(a)):
            if a[i] in vow:
                counta += 1

        for i in range(len(b)):
            if b[i] in vow:
                countb += 1

        return counta == countb


# https://leetcode.com/problems/determine-if-string-halves-are-alike/
