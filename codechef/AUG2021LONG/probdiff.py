from itertools import permutations, combinations, combinations_with_replacement
from bisect import (
    bisect_left,
    bisect_right,
)  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

tt = int(input())

for _ in range(tt):
    arr = list(map(int, input().split()))
    distinct = len(set(arr))
    if distinct == 4:
        print(2)
    elif distinct == 1:
        print(0)
    elif distinct == 3:
        print(2)
    elif distinct == 2:
        dd = {}
        for i in arr:
            dd[i] = dd.get(i, 0) + 1
        count_even = 0
        for v in dd.values():
            if v % 2 == 0:
                count_even += 1
        if count_even == 2:
            print(2)
        else:
            print(1)
