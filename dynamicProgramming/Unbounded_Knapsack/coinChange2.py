# Question
# Minimum Number of coins to make sum of the values from coin array to make it equal to given sum value

# https: // youtu.be/I-l6PBeERuc

# if only one array is given, then consider
# that array as a weight array.
# weight(wt) array => coin array
# value array is not given

INT_MAX = float("inf")

def coinChange1(coin, n, _sum):
    # n is length of coin array
    dp = [[0 for _ in range(_sum+1)] for i in range(n+1)]

    # INT_MAX - 1 , here -1 is done bcoz INT_MAX + 1 cannot 
    # be stored in int and some time gives error regrding that 

    # at array_size = 0 and all columns are filled with INT_MAX-1
    for col in range(_sum+1):
        dp[0][col] = INT_MAX - 1

    # at col = 0 from array_size 1 to len(coin array) is set to 0 
    # bcoz number of coins needed to make sum equal to zero
    for array_size in range(1, n+1):
        dp[array_size][0] = 0

    # now for the array_size = 1, let's say at col = 2, and coin array = [3, 2, 5]
    # if array)size is 1 then, arr[0] is present in the array i.e. 3
    # we want sum to be equal to 4 which is not possible ever.
    # so , we need to fill the n = 1 (second row) with INT_MAX -1 value
    for col in range(1, _sum+1):
        if col%coin[0] == 0:
            dp[1][col] = col//coin[0]
        else:
            dp[1][col] = INT_MAX - 1


    # filling the table 
    for i in range(1, n+1):
        for j in range(1, _sum+1):

            if coin[i-1] <= j:
                # if coin not included then dp[i-1][j]
                # if coin included then 1 + dp[i][j-coin[i-1]]
                dp[i][j] = min( dp[i-1][j], 1 + dp[i][j-coin[i-1]])

            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][_sum]


coin = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
_sum = 4
print(coinChange1(coin, len(coin), _sum))
