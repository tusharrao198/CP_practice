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
    n, a, b = map(int, input().split())
    st = input()
    cd = cs = 0
    # cd district # cs state
    for i in range(n):
        if st[i] == "0":
            cd += a
        elif st[i] == "1":
            cs += b
    print(cd + cs)
