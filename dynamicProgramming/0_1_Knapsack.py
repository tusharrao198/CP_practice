# using memoization
global mat


def knapsack(arr, wt, w, n):  # recursive approach with memoization
    mat = [[-1 for i in range(w + 1)] for j in range(n + 1)]
    if n == 0 or w == 0:
        mat[n][w] = 0
        return mat[n][w]

    if mat[n][w] != -1:
        return mat[n][w]

    if wt[n - 1] <= w:
        mat[n][w] = max(arr[n - 1] + knapsack(arr, wt, w - wt[n - 1], n - 1), knapsack(arr, wt, w, n - 1))
        return mat[n][w]

    elif wt[n - 1] > w:
        mat[n][w] = knapsack(arr, wt, w, n - 1)
        return mat[n][w]


def knapsack1(arr, wt, w, n):  # iterative approach
    mat = [[-1 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 and j == 0:
                mat[i][j] = 0

            elif wt[i - 1] <= j:
                mat[i][j] = max((arr[i - 1] + mat[i - 1][j - wt[i - 1]]),
                                mat[i - 1][j])

            elif wt[i - 1] > j:
                mat[i][j] = mat[i - 1][j]

    return mat[n][w]


arr = [1, 3, 4, 5]
wt = [1, 4, 5, 7]
n = len(arr)
# w = int(input())
w = 7

# print(mat)
print(knapsack(arr, wt, w, n))
print(knapsack1(arr, wt, w, n))
