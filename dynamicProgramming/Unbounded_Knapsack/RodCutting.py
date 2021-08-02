# Rod cutting problem
# https://youtu.be/SZqAQLjDsag

def unbounded_knapsack(price, length, max_length, n):  # iterative approach
    dp = [[-1 for i in range(max_length + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(max_length + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            # if values is considered, we consider it again at i
            # if value is not considered, we call at i-1
            elif length[i - 1] <= j:
                dp[i][j] = max(
                    (price[i - 1] + dp[i][j - length[i - 1]]),
                    dp[i - 1][j]
                )

            elif length[i - 1] > j:
                dp[i][j] = dp[i-1][j]

    return dp[n][j]


length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(length)
max_length = n

print(unbounded_knapsack(price, length, max_length, n))
