# using memoization
# global dp


def knapsack(arr, wt, w, n):  # recursive approach with memoization
    dp = [[-1 for i in range(w + 1)] for j in range(n + 1)]

    if n == 0 or w == 0:
        dp[n][w] = 0
        return dp[n][w]

    if dp[n][w] != -1:
        return dp[n][w]

    if wt[n - 1] <= w:
        dp[n][w] = max(arr[n - 1] + knapsack(arr, wt, w - wt[n - 1], n - 1), knapsack(arr, wt, w, n - 1))
        return dp[n][w]

    elif wt[n - 1] > w:
        dp[n][w] = knapsack(arr, wt, w, n - 1)
        return dp[n][w]


def knapsack1(arr, wt, w, n):  # iterative approach
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

    return dp[n][w]


# arr = [1, 3, 4, 5]
# wt = [1, 4, 5, 7]
# w = int(input())
# w = 7

arr = [359, 963, 465, 706, 146, 282, 828, 962, 492]
wt = [96, 43, 28, 37, 92, 5, 3, 54, 93]
w = 383

# arr = [468, 335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605,
#     903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323]
# wt = [4, 4, 5, 2, 2, 4, 9, 8, 5, 3, 8, 8, 10, 4, 2, 10, 9, 7, 6, 1, 3,
#     9, 7, 1, 3, 5, 9, 7, 6, 1, 10, 1, 1, 7, 2, 4, 9, 10, 4, 5, 5, 7]
# w =  841

n = len(arr)
# print(dp)
print(knapsack(arr, wt, w, n))
print(knapsack1(arr, wt, w, n))
