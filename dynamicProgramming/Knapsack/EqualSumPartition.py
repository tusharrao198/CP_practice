# find if an given array can be divided into equal sum partition
# 1. First point to note is, sum can be equally divided only when whole array sum is even otherwise not.
# 2. If first condition satisfies, then check for if sum(arr)/2 is present in the array or not.
# return True if present else: False

def subsetSum(arr, n, sum_) -> bool:
    dp = [[False for _ in range(sum_ + 1)] for i in range(n + 1)]
    # initialization
    for col in range(sum_+1):
        dp[0][col] = False

    # every row of column 0 is initialized with True because zero sum can be obtained in a subset of array when empty set is selected.
    for array_size in range(n+1):
        dp[array_size][0] = True

    # important dp[0][0] = True
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum_ + 1):

            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j - arr[i-1]]) or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum_]


def equalSumPartition(arr, n):
    _sum = sum(arr)
    if _sum % 2 != 0:
        return False
    return subsetSum(arr, n, _sum // 2)


arr = [8, 3, 5, 6]
n = len(arr)
print(equalSumPartition(arr, n))


