import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

# # accumulated sum
# def prefix_sum(arr):
#     # lst = [1, 2, 3, 4, 5, 6]
#     # return [1, 3, 6, 10, 15, 21]
#     prefix_sum = accumulate(arr)
#     return [i for i in prefix_sum]

inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    # n, a, b = map(int, inp().split())
    arr=list(map(int, inp().split()))

    arr.sort()
    ans = {}
    area = arr[0]*arr[4*n-1]
    for i in range(0,2*n):
        if arr[2*i] != arr[2*i+1] or arr[i]*arr[4*n-i-1]!=area:
            ans = 'NO'
    print(ans)