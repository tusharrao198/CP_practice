import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))
    for i in range(1, n):
        if arr[i]-arr[i-1]>3:
            print("NO")
            break
    else:
        print("YES")