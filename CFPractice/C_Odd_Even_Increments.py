import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))
    cc = 0
    dd = 0
    cc1 = 0
    dd1 = 0
    for i in range(n):
        if i%2==0:
            if arr[i]%2==0:
                dd+=1
            else:
                cc1+=1
        if i%2==1:
            if arr[i]%2==1:
                cc+=1
            else:
                dd1+=1
    
    if (cc+dd)==n or (cc1+dd1)==n or (dd+dd1)==n or (cc+cc1)==n:
        print("YES")
    else:
        print("NO") 
        
    