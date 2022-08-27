import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

inp = sys.stdin.readline
for _ in range(int(inp())):
    # n= int(inp())
    a, b = map(int, inp().split())

    if a%b==0:
        print(0)
        continue
        
    print(b- (a%b))
    