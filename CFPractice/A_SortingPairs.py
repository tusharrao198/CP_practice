import sys
inp=sys.stdin.readline
for __ in range(int(inp())):
    n=int(inp())
    arr=list(map(int,inp().split()))
    cnt=1
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            print('YES')
            cnt=0
            break
    if cnt!=0:
        print('NO')