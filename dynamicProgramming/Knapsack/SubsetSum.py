# to check if any subset with sum equal to sum_ value
def subsetSum(arr, n, sum_) -> bool:
    dp = [[False for _ in range(sum_ + 1)] for i in range(n + 1)]
    # initialization
    for col in range(sum_+1):
        dp[0][col] = False

    for array_size in range(n+1):
        dp[array_size][0] = True

    # important dp[0][0] = True
    dp[0][0] = True

    for i in range(n + 1):
        for j in range(sum_ + 1):

            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j - arr[i-1]]) or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum_]


wt = [1, 3, 4, 8]
wt = [3, 34, 4, 12]
sum_ = 9
# if arr is not given then consider weight as the array ( for context see knapsack function in 0_1_Knapsack.py
n = len(wt)
print(subsetSum(wt, n, sum_))