import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n, x, y = map(int, inp().split())

    # finding difference d in AP
    c = n
    while (y-x)%(c-1)!=0:
        c-=1
    diff = (y-x)//(c-1)
    # print(diff, c)

    ap_start = []
    num_req = n-c
    tmpx = x
    while num_req>0 and tmpx-diff>0:
        ap_start.append(tmpx-diff)
        tmpx-=diff
        num_req-=1
    
    ap_end=[]
    last = y
    while num_req>0:
        ap_end.append(last+diff)
        last+=diff
        num_req-=1

    # print(ap_start, ap_end)

    ans = []
    if len(ap_start)>0:
        ans.extend(ap_start)
    
    b = x
    while c>0 and b<=y:
        ans.append(b)
        b+=diff
        c-=1

    if len(ap_end)>0:   
        ans.extend(ap_end)

    for i in ans:   
        print(i, end=" ")
    print()
