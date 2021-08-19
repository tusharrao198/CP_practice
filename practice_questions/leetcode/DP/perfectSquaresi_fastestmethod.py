# https://leetcode.com/problems/perfect-squares/submissions/
# https://www.youtube.com/watch?v=1xfx6M_GqFk&t=815s

# https://gist.github.com/SuryaPratapK/e243e585ae0417797659c868fb7ea295

from math import sqrt


class Solution:

    # using legendre's theorem 3 - square theorem
    # 1. Every natural number can be represented as sum of 4 integer squares
    # 2. Every natural number can be represented as sum of 3 integer squares,
    ##  if this condition does not satisfies i.e 4**a(8*b + 7)
    # 3. if condition is satisfied i.e 4**a(8*b + 7) then ans is 4 perfect squares numbers

    # time complexity:- O(sqrt(n))

    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n

        # check if perfect square already
        ps = sqrt(n)
        if int(ps) == ps:
            return 1

        # check if 3 perfect squared condition satisfies i.e 4**a(8*b + 7)
        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        # if 4 does not satisfies then check for 2 and 3

        # check for 2
        i = 1
        while i * i <= n:
            y = n - i * i
            x = int(sqrt(y))
            if x * x == y:
                return 2
            i += 1

        # if nothing satisfies above then return 3
        return 3


#     # TC:- O(n*sqrt(n))
#     def numSquares(self, n: int) -> int:
#         dp = [i for i in range(n+1)]

#         if n<=3:
#             return n
#         for i in range(len(dp)):
#             j = 1
#             while (j*j<=n):
#                 dp[i] = min(dp[i], 1+ dp[i-j*j])
#                 j+=1
#         return dp[n]
