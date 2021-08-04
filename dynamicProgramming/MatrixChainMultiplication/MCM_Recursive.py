
global dp

# MCM Bottom UP  with DP Memoization
def MCM1(arr, i, j):
    if i>=j:
        return 0  

    if dp[i][j] != -1:
        return dp[i][j]    

    _min = float("inf") 
    # i =1 and j= len(arr) -1
    for k in range(i, j):  # k from i to <= j-1
        temp_ans = MCM1(arr, i, k) + (arr[i-1]*arr[k]*arr[j]) + MCM1(arr,k+1, j)
        _min = min(_min, temp_ans)
    dp[i][j] = _min
    return _min


def MCM(arr, i, j): # MCM Recursive TC => O(n**3)
    if i>=j:
        return 0

    _min = float("inf")
    for k in range(i, j):  # k from i to <= j-1
        print(i, k , j)
        temp = MCM(arr, i, k) + (arr[i-1]*arr[k]*arr[j]) + MCM(arr,k+1, j)
        _min = min(_min, temp)

    #------------same loop but with different approach for k
    # for k in range(i+1, j+1):  # k=i+1 to k<=j
    #     temp = MCM(arr, i, k-1) + (arr[i-1]*arr[k-1]*arr[j]) + MCM(arr,k, j)
    #     _min = min(_min, temp)

    return _min




# main
arr = [40, 20, 10, 30 ,10, 30]
i = 1
j = len(arr)-1
N = 1001 # arr.length given in constraints

dp = [[-1 for _ in range(N+1)]for __ in range(N+1)]

print(MCM1(arr, i, j))
