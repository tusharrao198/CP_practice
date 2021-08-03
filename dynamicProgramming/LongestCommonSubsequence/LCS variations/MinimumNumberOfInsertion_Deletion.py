# Minimum no. of insertion and deletion to convert a string a to b


# longestCommonSubsequence
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
    
    return dp[m][n]

def MinimumNumberOfInsertion_Deletion(x, y, m, n):
    _lcs = longestCommonSubsequence(x, y, m, n)
    deletion = m - _lcs
    insertion = n - _lcs
    print(deletion, insertion)


#  heap  -------------> pea
#    \               /
#    \              1 insertion (add p)
#  2 deletion      / 
#     \           /
#           ea 

x, y = 'heap', 'pea'
m, n = len(x), len(y)

# table initalized globally
dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

MinimumNumberOfInsertion_Deletion(x, y, m, n)
