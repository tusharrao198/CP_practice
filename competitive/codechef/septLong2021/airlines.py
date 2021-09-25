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
    a, b, c, d, e = map(int, input().split())
    if (a + b <= d) and c <= e:
        print("YES")
    elif a + c <= d and b <= e:
        print("YES")
    elif b + c <= d and a <= e:
        print("YES")
    else:
        print("NO")
