from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

# 'Locate the leftmost value exactly equal to x'
def leftmost_index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

# 'Find rightmost value less than x'
def find_lt(a, x):
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    return -1

# 'Find rightmost value less than or equal to x'
def find_le(a, x):
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    return -1

# 'Find leftmost value greater than x'
def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return -1

# 'Find leftmost item greater than or equal to x'
def find_ge(a, x):
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    return -1

# accumulated sum
def prefix_sum(arr):
    # lst = [1, 2, 3, 4, 5, 6]
    # return [1, 3, 6, 10, 15, 21]
    prefix_sum = accumulate(arr)
    return [i for i in prefix_sum]

# How to sort dictionary :-
# dd = {k: v for k, v in sorted(dd.items(), key=lambda x: x[1], reverse=True)}

# very handy and important
# sorted w.r.t frequency increasing order and then in decreasing order based on second lambda (x[0])
# " - " in lambda indicate sorting in descending order
# dd = {k: v for k, v in sorted(dd.items(), key=lambda x: (x[1], -x[0]))}
# https://stackoverflow.com/questions/5212870/sorting-a-python-list-by-two-fields

# https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes/4233482

# ------------------------------------------------------------- #
import sys
# from math import ceil, floor, gcd, sqrt, isqrt, pow, prod, log,
# from itertools import accumulate

## Sort Dictionary / Map
# sorted w.r.t frequency increasing order and then in decreasing order based on second lambda (x[0])
# " - " in lambda indicate sorting in descending order
# mp = {k: v for k, v in sorted(mp.items(), key=lambda x: (x[1], -x[0]))}

# to print a elements in a list in a single line
# print(*lst)
# for eg. lst = [1,2,3,4,5]
# output = 1 2 3 4 5

# accumulated sum
def prefix_sum(arr):
    # lst = [1, 2, 3, 4, 5, 6]
    # return [1, 3, 6, 10, 15, 21]
    prefix_sum = accumulate(arr)
    return [i for i in prefix_sum]

def freq(mp):
    mp ={}
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i], 0) + 1
    return mp
    
import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    n, a, b = map(int, inp().split())
    arr=list(map(int, inp().split()))
    
    ans = []
    for i in range(n):
        print(ans[i], end= " ")
    print()