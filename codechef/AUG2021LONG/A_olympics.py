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
    a1, a2, a3, a4, a5, a6 = map(int, input().split())
    if (a1 + a2 + a3) > (a4 + a5 + a6): print(1)
    else: print(2)
