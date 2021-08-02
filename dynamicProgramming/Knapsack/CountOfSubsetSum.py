# count of subset with given sum

def countOfSubsetSum(arr, n, _sum):
    dp = [[0 for _ in range(_sum + 1)] for i in range(n + 1)]

    # initialization

    # every row of column 0 is initialized with True because zero sum can be obtained
    # in a subset of array when empty set is selected.
    for col in range(_sum + 1):
        dp[0][col] = 0

    # if array size is zero then no subsets present i.e. no sum can be obtained
    for array_size in range(n + 1):
        dp[array_size][0] = 1

    # this condition already satisfied in above loop.
    # dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, _sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][_sum]


# arr = [2, 3, 4, 6, 5, 8, 10]
arr = [1, 6, 5, 11, 9]
n = len(arr)
_sum = 11
print(countOfSubsetSum(arr, n, _sum))
