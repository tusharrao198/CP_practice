# https://www.interviewbit.com/problems/distinct-subsequences/

import numpy as np


class Solution:
    def numDistinct(self, A, B):
        m, n = len(A), len(B)
        dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]

        for i in range(m + 1):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if A[j - 1] != B[i - 1]:
                    dp[i][j] = dp[i][j - 1]

                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

        # x = np.array(dp)
        # print(x)
        return dp[n][m]


s = Solution()
A = "rabbbit"
B = "rabbit"
x = s.numDistinct(A, B)
print(x)
