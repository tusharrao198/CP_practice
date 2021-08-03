# Longest Common Subsequence

global dp 
# LCS

def LCS(x, y, m, n): # recursive approach without memoization
    print("funcation called LCS")
    
    # base condition always check the least input possible to get base condition
    if n==0 or m==0: return 0

    if x[m-1]==y[n-1]:
        return 1 + LCS(x, y, m-1, n-1)
    
    else:
        return max(LCS(x, y, m-1, n), LCS(x, y, m, n-1))


def LCS1(x, y, m, n): # recursive approach with memoization ( Bottom Up)
    print("funcation called LCS1")

    if n==0 or m==0: return 0

    if dp[m][n] != -1:
        return x[m][n]

    if x[m-1]==y[n-1]:
        dp[m][n] = 1 + LCS(x, y, m-1, n-1)
        return dp[m][n]

    else:
        dp[m][n] = max(LCS(x, y, m-1, n), LCS(x, y, m, n-1))
        return dp[m][n]


def LCS2(x, y, m, n): # Iterative approach (Top Down)
    print("funcation called LCS2")
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

# time complexity reduced from exponential to O(n*m) space complexity-> O(n*m)

x, y = "abcdwrt", "abcefghw"
m, n  = len(x), len(y)

# table initalized globally
dp = [[-1 for _ in range(n+1)] for __ in range(m+1)]

print(LCS2(x, y, m, n))
