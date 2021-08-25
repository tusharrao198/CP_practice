from itertools import permutations, combinations, combinations_with_replacement
from typing import List
import string


# dd = {}
# for i, letter in enumerate(string.ascii_lowercase):
#     dd[letter] = i + 1


def solve(s, n, index):
    ans = True
    if index == -1:
        ans = False
    else:
        res = ord(s[index])
        l, r = index, index
        tracked = 1
        while tracked < n:
            if (l - 1) >= 0 and ord(s[l - 1]) == res + 1:
                tracked += 1
                l -= 1
                res += 1
            elif (r + 1) < n and ord(s[r + 1]) == res + 1:
                tracked += 1
                r += 1
                res += 1
            else:
                break
        if tracked < n:
            ans = False
    if ans:
        return "YES"
    return "NO"


tt = int(input())
for _ in range(tt):
    s = input()
    n = len(s)
    index = -1

    for i in range(n):
        if s[i] == "a":
            index = i
            break

    rr = solve(s, n, index)
    print(rr)
