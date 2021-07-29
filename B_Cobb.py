from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def main():
    tt = int(input())
    for _ in range(tt):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        a = arr[-1]
        b = arr[-2]
        ans = k * (a | b)
        print(((n-1)*(n-2)) - ans)

        

main()
