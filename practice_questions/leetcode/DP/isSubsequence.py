# https: // leetcode.com/problems/is-subsequence/submissions/

class Solution:

    dp = [[0 for _ in range(10000+1)] for __ in range(100+1)]

    def LCS(self, x, y, m, n):
        for c in range(n+1):
            self.dp[0][c] = 0

        for r in range(m+1):
            self.dp[r][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):

                if x[i-1] == y[j-1]:
                    self.dp[i][j] = 1 + self.dp[i-1][j-1]

                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])

        return self.dp[m][n]

    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        lcs = self.LCS(s, t, m, n)
        if lcs==len(s):
            return True
        return False
