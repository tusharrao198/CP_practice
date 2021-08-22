
def knapsack(arr, wt, w, n):  # iterative approach
    dp = [[-1 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif wt[i - 1] <= j:
                dp[i][j] = max(
                    (arr[i - 1] + dp[i - 1][j - wt[i - 1]]),
                    dp[i - 1][j]
                )

            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    res = dp[n][w]
    for i in range(w+1):
        if res==dp[n][i]:
            return f"{i} {res}"
    return dp[n][w]


wt = [13,19,16,12,10,12,13,15,11,16,0]
arr = [8,10,8,9,2,8,5,5,7,2,0]
# wt = [12,5,16,16,10,21,18,12,17,18] # cost of fair
# arr = [3,8,9,6,2,9,4,4,8,9] # fun
w = 50
n = 10

print(knapsack(arr, wt, w, n))

