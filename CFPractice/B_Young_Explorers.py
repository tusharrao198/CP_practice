import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))
        
    mp = {}
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i], 0) + 1

    mp = {k: v for k, v in sorted(mp.items(), key=lambda x: x[0])}
    sm=0
    rem=0
    for k in mp:
        mp[k]+=rem
        sm+=(mp[k]//k)
        rem=mp[k]%k
    print(sm)
