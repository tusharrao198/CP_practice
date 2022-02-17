import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))
    # arr.sort(reverse=True)
    
    mp = {}
    for i in range(n):
        mp[arr[i]] = mp.get(arr[i], 0) + 1
    ans = 0
    for k,v in mp.items():
        ans += (v//k)
    print(ans)