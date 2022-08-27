import sys
# import math
# from math import (ceil, floor, gcd, sqrt, prod, gcd, isqrt, inf, log, pow)
# from itertools import accumulate
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, inp().split())
        x.append(a)
        y.append(b)

    if x!=sorted(x) or y!=sorted(y):
        print("NO")
        continue
    
    if x[0]<0 or y[0]<0 or x[0]-0 <y[0]-0:
        print("NO")
        continue

    check = False

    for j in range(1, n):
        dx = x[j]-x[j-1]
        dy = y[j]-y[j-1]
        if dx>=0 and dy>=0 and dx>=dy:
            continue
        else:
            check =True
            break

    
    if check:
        print("NO")
        continue

    print("YES")


    
    

