from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

tt = int(input())
for _ in range(tt):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    _prev = lst[0]
    count = 0
    for i in range(1, len(lst)):
        if lst[i] < _prev:
            count+=1
        _prev = lst[i]
    if count+1==k: 
        print("Yes")
    else: 
        print("No")