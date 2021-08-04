# minimum Number of deletion in a string to make it Palindromic

# LPS is inversely proportional to no. of deletion

global dp


def longestPalindromicSubsequence(x, y, m, n):
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


def minDeletiontomakeStringPalindromic(x, y,m ,n):
    lps = longestPalindromicSubsequence(x, y, m, n)
    return m - lps

x = "AGGTAB"
# x = "agbcba"
m = len(x)

y = x[::-1]  # reverse of x
n = len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

print(minDeletiontomakeStringPalindromic(x, y , m , n))