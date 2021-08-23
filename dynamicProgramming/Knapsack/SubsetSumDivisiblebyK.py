# https://www.geeksforgeeks.org/number-of-subsets-with-sum-divisible-by-m-set-2/

# count of subset with given sum divisible by k

def countOfSubsetSumDivisiblebyK(arr, n, _sum, k):
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
    for i in dp:
        print(i)
    
    count = 0
    for i in range(1, _sum+1):
        print("A ",i , dp[n][i])
        if dp[n][i]>0:
            print("T ", i)
            if i%k==0:
                print("B ", i, dp[n][i])
                count+=dp[n][i]

    return count


# arr = [2, 3, 4, 6, 5, 8, 10]
# arr = [1, 6, 5, 2, 11, 9]
# n = len(arr)
# _sum = 11

# arr = [1, 2, 3]
arr = [3,3,3,3]
n = len(arr)
_sum = sum(arr)
k = 6
print(countOfSubsetSumDivisiblebyK(arr, n, _sum, k))
