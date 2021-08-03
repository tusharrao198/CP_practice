# minInsertiontomakeStringPalindromic

# minimum Number of Insertion in a string to make it Palindromic
# We previously solved minimum deletion required problem 
# where we found that LPS is inversely proportional to no. of deletion

# Here,  for insertion we observe that the numbers that are deleted does not have a pair 
# or appear twice in order to make them a plaindrome.

# from this we observe that, no.of insertions = no. of deletion

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


def minInsertiontomakeStringPalindromic(x, y, m, n):
    # no.of insertions = no. of deletion
    _lps = longestPalindromicSubsequence(x, y, m, n)
    return m - _lps


x = "AGGTAB"
# x = "agbcba"
m = len(x)

y = x[::-1]  # reverse of x
n = len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

print(minInsertiontomakeStringPalindromic(x, y, m, n))
