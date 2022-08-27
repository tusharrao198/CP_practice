# ------------------------------------------------------------- #
import sys
from math import ceil, floor, gcd, sqrt, isqrt, pow, prod
# from itertools import accumulate
from itertools import combinations
inp = sys.stdin.readline
for _ in range(int(inp())):
    # n= int(inp())
    a = []
    for i in range(3):
        x,y = map(int, inp().split())
        a.append([x, y])
    
    c = list(combinations(a, 2))

    a.sort(key=lambda x : -x[1])

    if a[0][1]==a[1][1]:
        print(abs(a[0][0]-a[1][0]))
    else:
        print(0)
