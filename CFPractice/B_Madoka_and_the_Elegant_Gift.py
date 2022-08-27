# ------------------------------------------------------------- #
import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

## Sort Dictionary / Map
# sorted w.r.t frequency increasing order and then in decreasing order based on second lambda (x[0])
# " - " in lambda indicate sorting in descending order
# mp = {k: v for k, v in sorted(mp.items(), key=lambda x: (x[1], -x[0]))}

# to print a elements in a list in a single line
# print(*lst)
# for eg. lst = [1,2,3,4,5]
# output = 1 2 3 4 5

# accumulated sum
# def prefix_sum(arr):
#     # lst = [1, 2, 3, 4, 5, 6]
#     # return [1, 3, 6, 10, 15, 21]
#     prefix_sum = accumulate(arr)
#     return [i for i in prefix_sum]

def freq(mp,arr):
    mp ={}
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i], 0) + 1
    return mp
    
inp = sys.stdin.readline
for _ in range(int(inp())):
    n, m = map(int, inp().split())
    a = []
    for i in range(n):
        a.append(list(map(int, inp().split())))
    
    flag=True

    for i in range(n-1):
        for j in range(len(a[i])-1):
            sm = (ord(a[i][j])-ord("0"))+(ord(a[i+1][j])-ord("0"))+(ord(a[i][j+1])-ord("0"))+(ord(a[i+1][j+1])-ord("0"))
            if sm ==3:
                flag=False
                break
        if not flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")

# print(ord("9")-ord("0"))