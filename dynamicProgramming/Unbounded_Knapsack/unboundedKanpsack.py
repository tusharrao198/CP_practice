# UNBOUNDED KNAPSACK

def unbounded_knapsack(val, wt, w, n):  # iterative approach
    dp = [[-1 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0


            # if values is considered, we consider it again at i
            # if value is not considered, we call at i-1
            elif wt[i - 1] <= j:
                dp[i][j] = max(
                    (val[i - 1] + dp[i][j - wt[i - 1]]),
                    dp[i - 1][j]
                )

            elif wt[i - 1] > j:
                dp[i][j] = dp[i-1][j]

    return dp[n][w]


# val = [1, 3, 4, 5]
# wt = [1, 4, 5, 7]
# w = int(input())
# w = 7

val = [10, 30, 20]
wt = [5, 10, 15]
w = 100

n = len(val)
print(unbounded_knapsack(val, wt, w, n))

