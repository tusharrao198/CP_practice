
# plaindromePartitioning with memoization Bottom Up DP

global dp

def isPalindrome(arr, i , j):
    # ss = arr[i:j+1]
    # if ss == ss[::-1]: return True
    # return False

    # Using two pointer to check palindrome
    while (i < j):
        if (arr[i] != arr[j]):
            return False
        i += 1
        j -= 1
    return True

def plaindromePartitioning(arr, i , j):
    if i >= j: return 0

    # if i==j: then it is already a plindrome so return 0

    if isPalindrome(arr, i, j): return 0

    if dp[i][j] != -1: return dp[i][j]

    _min = float("inf")
    # initially i =0 and j= len(arr) -1
    for k in range(i, j):  # k from i to <= j-1
        temp_ans = plaindromePartitioning(arr, i, k) + 1 + plaindromePartitioning(arr, k+1, j)
        _min = min(_min, temp_ans)    
    
    dp[i][j] = _min
    
    return _min


# main
arr = "ababbbabbababa"
# arr = "nitik"
i = 0
j = len(arr)-1
N = 1001  # arr.length given in constraints

dp = [[-1 for _ in range(N+1)]for __ in range(N+1)]

print(plaindromePartitioning(arr, i, j))
