global dp


def solve(arr, n, X, Y, i):

    if i >= n:
        return 0

    if dp[i][X][Y] != -1:
        return dp[i][X][Y]

    X_completed = 0
    Y_completed = 0
    excluded = 0

    if X >= arr[i]:
        X_completed = 1 + solve(arr, n, X - arr[i], Y, i + 1)

    if Y >= arr[i]:
        Y_completed = 1 + solve(arr, n, X, Y - arr[i], i + 1)

    excluded = solve(arr, n, X, Y, i + 1)

    dp[i][X][Y] = max(excluded, max(X_completed, Y_completed))

    return dp[i][X][Y]


arr = [6, 5, 5, 4, 3]
# arr = [6,5,2,1,8]
maxN, maxW = 1000, 1000
# x, y = 8, 9
X,Y = 17,5
dp = [[[-1] * maxW] * maxW] * maxN

dp = [[[-1 for _ in range(Y+1)] for kk in range(X+1)] for jj in range(n+1)]

n = len(arr)
print(solve(arr, n, X, Y, 0))
