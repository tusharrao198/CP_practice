from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right   # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt

tt = int(input())
for _ in range(tt):
    # n, a, b = map(int, input().split())
    # lst = list(map(int, input().split()))
    n = int(input())
    num = floor(n+1)//10
    print(num)

