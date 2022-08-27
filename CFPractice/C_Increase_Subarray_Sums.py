import sys
inp = sys.stdin.readline

def maxSumSubarray(arr, n, k):
    i = j = 0
    mx = float("-inf")
    s = 0
    while k>0 and i<=j and j < n:
        s += arr[j]
        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            mx = max(s, mx)
            s -= arr[i]
            i += 1
            j += 1
    return mx

for _ in range(int(inp())):
    n, x = map(int, inp().split())
    a=list(map(int, inp().split()))

    smm = [-1] * (n+1)
    for i in range(n+1):
        smm[i] = maxSumSubarray(a, n, i)

    for k in range(n+1): 
        finalmx = 0
        for i in range(1, n+1):
            finalmx = max(finalmx, smm[i]+min(i, k)*x)
        print(finalmx, end=" ")
    print()