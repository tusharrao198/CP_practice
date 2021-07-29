from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def main():
    tt = int(input())
    for _ in range(tt):
        n = int(input())
        arr = list(set(list(map(int, input().split()))))
        dd = {}
        mx = max(arr)  
        for i in range(n):
            dd[arr[i]] = abs(mx - arr[i])
        dd = {k: v for k, v in sorted(dd.items(), key=lambda x: x[1])}
        for k,v in dd.items():
            return k*mx            
        return -1

print(main())
