# longestCommonSubstring
global dp


def longestCommonSubstring(x, y, m, n):
    # table initalized globally
    dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

    for c in range(n + 1):
        dp[0][c] = 0

    for r in range(m + 1):
        dp[r][0] = 0

    ans = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])

            else:
                dp[i][j] = 0

    return ans


# ------------------------- Below Apporach space optimized ---------------
# https: // www.geeksforgeeks.org/longest-common-substring-dp-29/
# with complexities
# Time Complexity: O(n*m)
# Auxiliary Space: O(min(m, n))

# Function to find the length of the
# longest LCS
def LCSubStr(s, t, n, m):
    # Create DP table
    dp = [[0 for i in range(m + 1)] for j in range(2)]
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (s[i - 1] == t[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0
    return res


x, y = "OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com"

# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)

m, n = len(x), len(y)

print(longestCommonSubstring(x, y, m, n))

print(LCSubStr(x, y, m, n))
