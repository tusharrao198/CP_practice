# ------------------------------------------------------------- #
import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    # n, a, b = map(int, inp().split())
    a=list(map(int, inp().split()))
    fin = []
    mp ={}
    for i in range(n):
        mp[a[i]] = mp.get(a[i], 0) + 1
    
    val = 0
    for k, v in mp.items():
        if v>1:
            val+=(v-1)
    
    ans = n 
    for i in range(n):
        if val>0:
            fin.append(ans)
            ans-=1
            val-=1
        else:
            fin.append(ans)

    for i in range(n-1,-1,-1):
        print(fin[i], end= " ")
    print()