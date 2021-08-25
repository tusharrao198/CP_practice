from itertools import permutations, combinations, combinations_with_replacement
# https: // docs.python.org/3/library/bisect.html
from bisect import bisect_left, bisect_right
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

tt = int(input())
for _ in range(tt):
    cols = int(input())
    a = input()
    b = input()
    mat = [[_ for _ in a], [i for i in b]]
    cc = 0
    for i in range(cols):
        if mat[1][i]=="1":
            if mat[0][i]=="0":
                cc += 1

            elif i-1 >= 0 and mat[0][i-1] == "1":
                mat[0][i-1]="0"
                cc += 1
            
            elif i+1<cols and mat[0][i+1]=="1":
                mat[0][i+1]="0"
                cc += 1
        else:
            continue

    print(cc)        
