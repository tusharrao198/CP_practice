# Question
# Maximum Number of ways to make sum of the values from coin array to make it equal to given sum value 

# https://youtu.be/I4UR2T6Ro3w

# if only one array is given, then consider 
# that array as a weight array.
# weight(wt) array => coin array
# value array is not given 


def coinChange1(coin, n, _sum):
    # n is length of coin array
    dp = [[0 for _ in range(_sum+1)] for i in range(n+1)]

    for col in range(_sum+1):
        dp[0][col] = 0

    for array_size in range(n+1):
        dp[array_size][0] = 1

    # also dp[0][0] should be 1 bcoz, number of ways to get sum 0 with array_size 0 is 1 (i.e we can take empty setor null set)
    # dp[0][0] = 1   # already set to 1 in above loop

    for i in range(1, n+1):
        for j in range(1, _sum+1):

            if coin[i-1]<=j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin[i-1]]

            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[n][_sum]


coin = [1, 2, 3]
_sum = 4
print(coinChange1(coin, len(coin), _sum))
                
