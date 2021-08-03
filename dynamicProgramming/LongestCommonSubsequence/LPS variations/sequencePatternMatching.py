# sequencePatternMatching

# Given a string a and b, find that if a is a subsequence of b.
global dp

# Longest Common Subsequence
def LCS(x, y, m, n):
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

    return dp[m][n]


def sequencePatternMatching(x, y, m, n):
    lcs = LCS(x, y, m, n)
    if lcs==len(x):
        return True
    return False


x, y = "axy", "acxdfy"
m, n = len(x), len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

print(sequencePatternMatching(x, y, m, n))

