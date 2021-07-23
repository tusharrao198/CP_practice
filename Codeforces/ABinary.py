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
    # n, a, b = map(int, input().split())
    # lst = list(map(int, input().split()))
    n = int(input())
    ans = float("-inf")
    for c in list(str(n)):
        ans = max(int(c), ans)
    print(ans)
