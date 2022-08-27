import sys
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    a=list(map(int, inp().split()))
    if a==sorted(a):
        print(0)
        continue

    if(a[-1]<0 or a[-1]<a[-2]):
        print(-1)
        continue

    print(n-2)

    for i in range(n-2):
        print(i+1,n-1,n)
