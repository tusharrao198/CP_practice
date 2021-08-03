# https://leetcode.com/problems/pascals-triangle/submissions/

from math import factorial as f

# Formula
# The formula to find the entry of an element in the nth row and kth column of a pascal’s triangle is given by:

# (nk). The elements of the following rows and columns can be found using the formula given below.

# (nk) = (n−1k−1)+(n−1k)

# Here, n is any non-negative integer and 0 ≤ k ≤ n.

# The above notation can be written as:

# (nk)(i.e., n choose k) = C(n, k) = nCk = n!/ [k!(n – k)!]

# This pattern of getting binomial coefficients is called Pascal’s rule.

from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def f(n):
            if n==1 or n==0: return 1
            return n*f(n-1)
        res = []
        for i in range(numRows):
            lst = []
            for j in range(i+1):
                x = f(i)//(f(j) * f(i-j))
                lst.append(x)
            res.append(lst)
        return res

s = Solution()
x = s.generate(5)
print(x)
