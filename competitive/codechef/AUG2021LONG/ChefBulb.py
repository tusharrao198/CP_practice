from itertools import permutations, combinations, combinations_with_replacement
from typing import List
from math import ceil, floor, gcd, sqrt
from itertools import accumulate

tt = int(input())
for _ in range(tt):
    n, p, k = map(int, input().split())
    ans = 0
    rem = (p%k)   
    rem = rem-1

    quotient = (n-1)//k  # 
    full_pairs = (n-1) - (quotient * k)

    if rem > full_pairs: 
        ans  += (full_pairs  + 1) * (quotient + 1) + (quotient* (rem-full_pairs))

    else:
        ans += (rem + 1) * (quotient + 1)   

    for i in range(rem+1, n, k):
        ans+=1
        if i==p:
            print(ans)
    

    
    


    

