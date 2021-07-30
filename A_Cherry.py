from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def main():
    tt = int(input())
    for _ in range(tt):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = float("-inf")
        for i in range(1, n):
            ans = max(ans, arr[i-1]*arr[i])
        print(ans)


main()
