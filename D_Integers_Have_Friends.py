from itertools import permutations, combinations, combinations_with_replacement
from bisect import bisect_left, bisect_right  # https: // docs.python.org/3/library/bisect.html
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate



tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))
    # ans = -1
    # for i in [2, 3, 5, 7]:
    #     ce, co = 0, 0
    #     for j in range(n):
    #         if lst[j]%2==0: 
    #             ce+=1
    #         elif lst[j]%i: 
    #             co+=1

    for i in range(n):
        print(lst[i]%7)    

    # print(max(co, ce))

    
