import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))    
    
    o = []
    e = []

    for i in range(n):
        if arr[i]%2==0:
            e.append(arr[i])
        else:
            o.append(arr[i])  

    if o==sorted(o) and e==sorted(e):
        print("Yes")
    else:
        print("No")