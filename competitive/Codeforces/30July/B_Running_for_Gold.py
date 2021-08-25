from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def compare(a, b):
    c= 0
    for i in range(5):
        if a[i]<b[i]:
            c+=1
    return c>=3

def solve(dd, n):
    winner = 1
    for i in range(2, n+1):
        if compare(dd[i], dd[winner]):
            winner = i

    for i in range(1,n+1):
        if compare(dd[i], dd[winner]):
            winner = -1
            break
    print(winner)


tt = int(input())
for _ in range(tt):
    n = int(input())
    dd = {}
    for __ in range(1, n+1):
        dd[__] =  list(map(int, input().split()))
    solve(dd, n)