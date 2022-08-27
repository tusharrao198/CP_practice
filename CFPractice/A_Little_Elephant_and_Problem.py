import sys
# from math import ceil, floor, gcd, sqrt
# from itertools import accumulate
inp = sys.stdin.readline
# for _ in range(int(inp())):
n= int(inp())
a=list(map(int, inp().split()))

if n==1:
    print("YES")
elif n==2 and a[0]<=a[1]:
    print("YES")
else:
    x= [-1, -1]
    y= [-1, -1]
    for i in range(1, n-1):
        if a[i-1]<a[i]<a[i+1]:
            x[0] = i
            x[1] = a[i]
        
        elif a[i-1]<a[i]>a[i+1]:
            y[0] = i
            y[1] = a[i]
        # print(a[i-1],a[i],a[i+1])
    
    print(x, y)
