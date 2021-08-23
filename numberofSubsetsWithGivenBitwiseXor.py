# to check if any subset with sum equal to sum_ value
def subsetSum(arr, n, sum_) -> bool:
    dp = [[0 for _ in range(sum_ + 1)] for i in range(n + 1)]

    # initialization
    for col in range(sum_+1):
        dp[0][col] = 0

    for array_size in range(n+1):
        dp[array_size][0] = 1

    # important dp[0][0] = 1
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, sum_ + 1):

            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j - arr[i-1]]) + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    for i in dp:
        print(i)
    
    

    return dp[n][sum_]


# wt = [1, 3, 4, 8]
# wt = [3, 34, 4, 12]
# wt = [35, 54, 100, 19, 39, 1, 89, 28, 68, 29, 94]
# sum_ = 649
# # if arr is not given then consider weight as the array ( for context see knapsack function in 0_1_Knapsack.py
# n = len(wt)

wt = [1, 2, 3]
n = len(wt)
sum_ = 6

print(subsetSum(wt, n, sum_))
