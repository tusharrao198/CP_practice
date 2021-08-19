from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    _avg = lst[0]
    b= lst[1:]
    b_size = n-1
    _avg += sum(b)/b_size
    print("{0:.9f}".format(_avg))
