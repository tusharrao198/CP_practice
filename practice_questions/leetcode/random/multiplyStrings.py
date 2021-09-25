# https://leetcode.com/problems/multiply-strings/submissions/


class Solution:
    def number(self, dd, num):
        n = 0
        for i in num:
            if i == 0:
                n = dd[i]
            else:
                n = n * 10 + dd[i]
        return n

    def multiply(self, num1: str, num2: str) -> str:
        dd = {str(i): i for i in range(0, 10)}
        n = self.number(dd, num1)
        m = self.number(dd, num2)
        return str(n * m)
