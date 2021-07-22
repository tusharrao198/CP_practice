from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt


def find(s, t):
    lst = []
    i = 0
    while i < len(s):
        if s[i]==t[0]:
            lst.append(i)
        i += 1
    return lst


def find2(s, j, t):
    r = len(s) - 1
    for i in range(1, len(t)):
        if j > 0 and s[j - 1] == t[i]:
            j -= 1
        elif j < r and s[j + 1] == t[i]:
            j += 1
        else:
            return False
    return True


tt = int(input())
for _ in range(tt):
    # n, a, b = map(int, input().split())
    # lst = list(map(int, input().split()))
    s = input()
    t = input()
    lst = find(s, t)
    print(lst)
    ans = "NO"
    for j in lst:
        if find2(s, j, t):
            sol = "YES"
            break
    print(ans)
