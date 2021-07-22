# https://leetcode.com/problems/add-strings/submissions/


class Solution:
    def number(self, num):
        dd = {str(i): i for i in range(0, 10)}
        n = 0
        for i in num:
            if i == 0:
                n = dd[i]
            else:
                n = n * 10 + dd[i]
        return n

    def addStrings(self, num1: str, num2: str) -> str:
        n = self.number(num1)
        m = self.number(num2)

        return str(n + m)
