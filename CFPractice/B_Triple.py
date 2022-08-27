import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    lst=list(map(int, inp().split()))
    mp = {}
    for i in range(n):
        mp[lst[i]] = mp.get(lst[i], 0) + 1
    mp = {k: v for k, v in sorted(mp.items(), key=lambda x: (-x[1], -x[0]))}

    for k, v in mp.items():
        if v>=3:
            print(k)
            break
    else:
        print("-1")
        
        
        
    