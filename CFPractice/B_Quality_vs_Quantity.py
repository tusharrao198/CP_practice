import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    a=list(map(int, inp().split()))
    a.sort()
    cb = 0
    cr = 0
    i = 1
    j = n-1
    sr = a[j]
    sb = a[0]+a[1]

    f = False
    while i<j:
        if sr>sb:
            f=True
            break            
        sr+=a[j-1]
        j-=1

        sb+=a[i+1]
        i+=1
    
    if f:
        print("YES")
    else:
        print("NO")