from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt


def index(a, x):
    # 'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1


def find_lt(a, x):
    # 'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    return -1


def find_le(a, x):
    # 'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    return -1


def find_gt(a, x):
    # 'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return -1


def find_ge(a, x):
    # 'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    return -1


tt = int(input())
for _ in range(tt):
    h, w = map(int, input().split())
    # lst = list(map(int, input().split()))
    # num = int(input())

    mat = [] # first and last row
    for i in range(w):
        if i%2==0:
            mat.append("1")
        else:        
            mat.append("0")
    # print(mat)
    mat = "".join(mat)

    midrow0 = "".join(["0" for _ in range(w)])
    midrow2 = '1' + '0'*(w-2) + '1'
    # midrow2 = []
    # x = h//2
    # if (x+1!=h-1) and (x-1!=0):
    #     for i in range(w):
    #         if i == 0 or i==w-1:
    #             midrow2.append("1")
    #         else:
    #             midrow2.append("0")
    # # print("MID = ", midrow2)

    # midrow2 = "".join(midrow2)

    ans = ['0' for _ in range(h)]
    l = 0
    r = h-1
    while l<=r:
        if l==0:
            ans[l] = ans[r] = mat
            # print(ans)

        elif (l+1==r) and (l%2==0):
            ans[l] = midrow2
            ans[r] = midrow0
            # print("A ", ans)

        elif l % 2 == 1:
            ans[l] = midrow0
            ans[r] = midrow0
            # print("B ", ans)

        else:
            ans[l] = midrow2
            ans[r] = midrow2
            # print("C ", ans)


        l+=1
        r-=1
    # print(ans)

    for k in ans:
        print(k)
    print()

        




        
        











