# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        _sum = 0
        for i in str(n):
            x = int(i)
            prod *= x
            _sum += x

        return prod - _sum
