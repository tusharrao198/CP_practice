# Longest Repeating Subsequence

# Given a string x, find the longest repeating subsequence (relative order)

# Approach:-
# To relate with previous problems, we consider the same string twice
# i.e. x and y is same.

# if we find LCS of x and y will be equal to x.
# consider example x = "AABECDD" and y=x
# LCS of x and y = x
# So, if cross-matching is available, then it is possible to
# consider that character, otherwise we will not,
# cross matching is necessary bcoz every other letter repeats twice
# but  E and C does not repeat ( their cross matching is not available for E and C)
#
# Hence, if we consider i index of x and j index for y
# then, what we understood is i==j is not allowed.


def longestRepeatingSubsequence(x, y, m, n):

    for c in range(n + 1):
        dp[0][c] = 0

    for r in range(m + 1):
        dp[r][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if x[i - 1] == y[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# x, y = "abcdwrt", "abcefghw"
# x = "AABEBCDD"
# x = "ABBA"
x = "abcdwrt"
y = x
m, n = len(x), len(y)

# table initalized globally
dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

print(longestRepeatingSubsequence(x, y, m, n))
