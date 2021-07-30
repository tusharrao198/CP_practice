from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate


def index(a, x):
    # 'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1


def find_lt(a, x):
    # 'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    return -1


def find_le(a, x):
    # 'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i - 1]
    return -1


def find_gt(a, x):
    # 'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    return -1


def find_ge(a, x):
    # 'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    return -1


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


def main():
    tt = int(input())
    for _ in range(tt):
        n, a, b = map(int, input().split())
        lst1 = list(map(int, input().split()))
        lst2 = list(map(int, input().split()))
        target = int(input())
        ans = ""
        print(ans)


main()
