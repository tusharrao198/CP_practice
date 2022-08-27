import sys
# from itertools import permutations, combinations, combinations_with_replacement
# from math import ceil, floor, gcd, sqrt
# from itertools import accumulate
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    a = []
    for i in range(n):
        a.append(i+1)
    
    a = a[::-1]

    for i in range(n-1, -1, -1):
        for j in range(n):
            print(a[j], end= " ")
        
        if i!=0:
            a[i], a[i-1] = a[i-1], a[i]

        print()
    



    
