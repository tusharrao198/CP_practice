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
    
    return dp

def minimumSubsetDifference(arr, n, _sum):

    dp = subsetSum(arr, n, _sum)

    # now table is filled with all the values needed.
    # so now we get the last row from it bcoz it contains the condition
    # which one of number can be utilised to get a subset sum from the given array.
    # we return only half of the array (S1) and other S2 = Range - 2*S1 .
    # So we need to find only half of the row from starting.
    
    lst = [] # contains value with True from the last row
    S1 = dp[n][:_sum//2+1]
    for i in range(len(S1)):
        if S1[i]:
            lst.append(i)
    print(lst)
    _min = float("inf")
    for i in range(len(lst)):
        _min = min(_min, _sum-2*lst[i])
    return _min
    


# arr = [2, 3, 4, 6, 5, 8, 10]
arr = [1, 6, 5, 11, 9]
arr = [1, 2, 7]
n = len(arr)
_sum = 11
print(minimumSubsetDifference(arr, n, _sum))
