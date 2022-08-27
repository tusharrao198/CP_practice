import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate
inp = sys.stdin.readline
for _ in range(int(inp())):
    # n= int(inp())
    n, s = map(int, inp().split())
    print(s//(n**2))