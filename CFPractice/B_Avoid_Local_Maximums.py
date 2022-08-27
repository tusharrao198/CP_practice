import sys
from math import ceil, floor, gcd, sqrt
from itertools import accumulate
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    # n, a, b = map(int, inp().split())
    a=list(map(int, inp().split()))

    cnt = 0
    for i in range(1, n-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            cnt+=1
            a[i+1]= max(a[i+1], a[i])
            if i+2<n:
                a[i+1] = max(a[i+1], a[i+2])
            

    print(cnt)
    for i in a:
        print(i, end=" ")
    print()
