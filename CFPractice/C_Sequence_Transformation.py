# import sys
# # from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# # from itertools import accumulate

# inp = sys.stdin.readline
# for _ in range(int(inp())):
#     n= int(inp())
#     arr=list(map(int, inp().split()))
    
#     s = len(set(arr))

#     if s==n:
#         if s==1:
#             print(0)
#             continue
#         if s>1:
#             print(1)
#             continue
#     else:
    
    
#     mp ={}
#     for i in range(n):
#         mp[arr[i]] = mp.get(arr[i], 0) + 1    
#     # mp = {k: v for k, v in sorted(mp.items(), key=lambda x: (x[1], -x[0]))}

#     ans = []
#     for i in range(n):
#         print(ans[i], end= " ")
#     print()