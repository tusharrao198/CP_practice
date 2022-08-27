from audioop import reverse
import sys
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))
    ans = 0
    for i in arr:
        ans|=i
    print(ans)

