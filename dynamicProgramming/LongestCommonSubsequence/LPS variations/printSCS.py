# ShortestCommonSubsequence
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


def printShortestCommonSubsequence(x, y, m, n):
    # fill table
    longestCommonSubsequence(x, y, m, n)

    _str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            _str += x[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                _str += x[i-1]
                i -= 1
            else:
                _str += y[j-1]
                j -= 1

    while i > 0:
        _str += x[i-1]
        i -= 1

    while j > 0:
        _str += y[j-1]
        j -= 1

    return _str[::-1]


# x, y = 'abcdfgh', 'abcefgh'
x, y = 'heap', 'pea'
# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)

m, n = len(x), len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

print(printShortestCommonSubsequence(x, y, m, n))
