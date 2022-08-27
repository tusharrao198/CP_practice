import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    s = str(n)
    l = len(s)
    ucnt = 0
    for i in s:
        if i!="0":
            ucnt+=1

    ans = []
    x = l
    c = 10
    while x>0:
        if n%c!=0:
            ans.append(n%c)
            n-=(n%c)
        c*=10
        x-=1

    print(ucnt)
    for i in ans:
        print(i, end=" ")
    print()