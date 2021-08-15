# https://leetcode.com/problems/sort-integers-by-the-power-value/


class Solution:
    def power(self, n):
        p = 0
        x = n
        while x != 1 and x > 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            p += 1
        return p

    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = []
        for i in range(lo, hi + 1):
            powers.append([i, self.power(i)])

        powers.sort(key=lambda x: (x[1], x[0]))
        return powers[k - 1][0]
