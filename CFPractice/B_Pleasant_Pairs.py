import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    a=list(map(int, inp().split()))

    cnt = 0
    for i in range(1, n+1):
        for j in range(a[i-1]-i, n+1, a[i-1]):
            if j>=0 and i<j and a[i-1]*a[j-1]==i+j:
                cnt+=1
    print(cnt)