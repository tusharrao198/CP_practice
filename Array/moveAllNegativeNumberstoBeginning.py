# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

def solve(arr, n):
    i = 0
    j = n-1
    while (i <= j):
        if arr[i] < 0:
            i += 1

        elif arr[i] >= 0 and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        elif arr[i] >= 0 and arr[j] >= 0:
            j -= 1
    return arr


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

n = len(arr)
print(solve(arr, n))
