from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def main():
    tt = int(input())
    for _ in range(tt):
        n = int(input())
        athlete_number = [float("inf")] *5
        index = [-1] * 5
        for __ in range(n):
            lst = list(map(int, input().split()))
            for i in range(5):
                if lst[i] < athlete_number[i]:
                    athlete_number[i] = lst[i]                
                    index[i] = __ + 1
        dd = {}
        for i in index:
            dd[i] = dd.get(i, 0) + 1

        # dd = {k: v for k, v in sorted(dd.items(), key=lambda x: x[1], reverse=True)}

        vals = list(dd.values())
        _max = max(vals)
        ans = []
        for i in vals:
            if i == _max:
                ans.append(i)
        
        if len(ans)==1:
            for k, v in dd.items():
                if v==ans[0]:
                    print(k)
                    break
        else:
            print(-1)
main()
