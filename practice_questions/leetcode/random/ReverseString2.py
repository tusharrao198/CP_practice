# not right code not submiited

# https://leetcode.com/problems/reverse-string-ii/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        first_k = s[:2][::-1]
        first_k.extend(s[2:])
        return "".join(first_k)
