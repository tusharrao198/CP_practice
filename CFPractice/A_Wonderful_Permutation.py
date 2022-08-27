import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n, k = map(int, inp().split())
    arr = list(map(int, inp().split()))
    cnt = 0
    s = {i+1 for i in range(k)}
    for i in range(k):
        if arr[i] not in s:
            cnt+=1
    print(cnt)