# https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/


class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        return " ".join([a[_][::-1] for _ in range(len(a))])
