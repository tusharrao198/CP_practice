import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

inp = sys.stdin.readline
for _ in range(int(inp())):
    # n= int(inp())
    n, x = map(int, inp().split())
    arr=list(map(int, inp().split()))
    mp ={}
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i], 0) + 1

    arr.sort()
    ans = 0
    for i in range(n-1, -1, -1):
        c =arr[i]
        d = c//x
        if mp[c]==0:
            continue
        if c%x!=0:
            ans+=mp[c]
            mp[c]=0
        else:
            
            # print(mp[c], mp[d])
            if (mp[c]>mp[d]):
                ans = ans + (mp[c]-mp[d])
                mp[c]=0
                mp[d]=0
            else:
                mp[d]-=mp[c]
                mp[c]=0

    print(ans)
