from math import comb

# https://leetcode.com/problems/pascals-triangle-ii/submissions/

# Formula
# The formula to find the entry of an element in the nth row and kth column of a pascal’s triangle is given by:

# (nk). The elements of the following rows and columns can be found using the formula given below.

# (nk)=(n−1k−1)+(n−1k)

# Here, n is any non-negative integer and 0 ≤ k ≤ n.

# The above notation can be written as:

# (nk) (i.e., n choose k) = C(n, k) = nCk = n!/[k!(n – k)!]

# This pattern of getting binomial coefficients is called Pascal’s rule.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # to find elements of nth Row
        lst = [1] * (rowIndex+1)
        for k in range(1, rowIndex):
            x = comb(rowIndex-1, k) + comb(rowIndex-1, k-1)
            lst[k] = x
        return lst
