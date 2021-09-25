# maxSumSubarray of size k
def maxSumSubarray(arr, n, k):
    i = j = 0
    mx = float("-inf")
    s = 0
    while j < n:
        s += arr[j]
        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            mx = max(s, mx)
            s -= arr[i]
            i += 1
            j += 1
    return mx


arr = [3, 1, 8, 4, 1, 2]
n = len(arr)
k = 3

print(maxSumSubarray(arr, n, k))
