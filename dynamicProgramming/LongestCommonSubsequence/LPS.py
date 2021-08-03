# LongestPalindromicSubsequence

# Question:- Given a string x, find the longest palindromic subsequence.

# Approach:-  We approache the problem using LCS, but if we take a look 
# we are only given 1 string x, So in order to apply LCS we need to have 
# a second string too. 

# Palindromic means same string when read from reverse or front.

# we create a second string y as function of a, i.e. b = reverse(a)
# and then simply apply LCS and you get the longest palindromic subsequence possible.

# Code:- 

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


# x = "AGGTAB"
x = "agbcba"
m = len(x)

y = x[::-1]  # reverse of x
n = len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

print(longestPalindromicSubsequence(x, y, m, n))
