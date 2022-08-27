import sys
# from math import ceil, floor, gcd, sqrt
# from itertools import accumulate
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= inp()

    a = set()
    a.add(n[0])

    cnt = 0
    for i in range(1, len(n)):
        if n[i]=="R":
            if "r" in a:
                cnt+=1
        elif n[i]=="G":
            if "g" in a:
                cnt+=1
        elif n[i]=="B":
            if "b" in a:
                cnt+=1
        
        a.add(n[i])
    
    if cnt==3:
        print("YES")
    else:
        print("NO")
        
