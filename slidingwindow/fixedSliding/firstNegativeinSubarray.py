# first Negative in Subarray of size k
from collections import deque as queue


def firstNegativeinSubarray(arr, n, k):
    i = j = 0
    q = queue()  # Initializing a queue
    ans = []
    while j < n:

        # removing elements which are smaller than the number to be added
        while len(q) > 0 and arr[j] < 0 and q[-1] < arr[j]:
            q.pop()

        if arr[j] < 0:
            q.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if len(q) == 0:
                ans.append(0)
            else:
                ans.append(q[0])

            if len(q) > 0 and arr[i] == q[0]:
                x = q.popleft()
                # print(x)

            i += 1
            j += 1
        # print(ans, q)
    return ans


arr = [12, -1, -7, 8, -15, 30, 16, 28]
n = len(arr)
k = 3

print(firstNegativeinSubarray(arr, n, k))
