import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    b=list(map(int, inp().split()))
    
    pos = n-1

    while pos>0 and b[pos-1]>=b[pos]:
        pos-=1

    while pos>0 and b[pos-1]<=b[pos]:
        pos-=1
        
    print(pos)
    