# ShortestCommonSubsequence

# Approach:- m + n - LCS

global dp


def longestCommonSubsequence(x, y, m, n):
    for c in range(n+1):
        dp[0][c] = 0

    for r in range(m+1):
        dp[r][0] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):

            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])



def shortestCommonSupersequence(m, n):

    # fill table
    longestCommonSubsequence(x, y, m, n)
    # m + n - LCS
    return m + n - dp[m][n]


# x, y = 'abcdfgh', 'abcefgh'
x, y = "AGGTAB", "GXTXAYB"
m, n = len(x), len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

print(shortestCommonSupersequence(m, n))

