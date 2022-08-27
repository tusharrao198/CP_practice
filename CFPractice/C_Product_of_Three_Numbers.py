import sys
from math import ceil
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    s = n

    x = ceil(n**(1/3))
    ans = set()

    # three numbers product is always in the range n**(1/3)
    for a in range(2, x+1):
        if n%a==0:
            ans.add(a)
            n//=a
            break

    # two numbers product is always in the range n**(1/2)
    for b in range(a+1, ceil(n**(1/2))+1):
        if n%b==0:
            ans.add(b)
            n//=b
            break     
    
    ans.add(n)
    if len(ans)==3:
        p = 1
        for i in ans:
            p*=i
        if p==s:
            print("YES")
            for i in ans:
                print(i, end=" ")
            print()
    else:
        print("NO")  