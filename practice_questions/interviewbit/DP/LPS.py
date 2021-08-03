class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        global dp
        B = A[::-1]
        m, n = len(A), len(A)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for c in range(n+1):
            dp[0][c] = 0

        for r in range(m+1):
            dp[r][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):

                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
