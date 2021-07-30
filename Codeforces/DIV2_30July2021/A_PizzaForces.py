from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def prefix_sum(arr): # cumulative sum
    # lst = [1, 2, 3, 4, 5, 6]
    # return [1, 3, 6, 10, 15, 21]
    prefix_sum = accumulate(arr)
    return [i for i in prefix_sum]

# How to sort dictionary :-
# dd = {k: v for k, v in sorted(dd.items(), key=lambda x: x[1], reverse=True)}



tt = int(input())
for _ in range(tt):
    n = int(input()) 
    ans = 0
    if n <=6: print(15) 
    else:
        if n%2==0: print((n*5)//2)
        else: print(((n+1)*5)//2)
