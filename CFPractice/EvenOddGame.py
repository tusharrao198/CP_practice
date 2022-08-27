import sys
inp = sys.stdin.readline

for __ in range(int(inp())):
    n=int(inp())
    a=list(map(int,inp().split()))
    cnt1,cnt2, sm = 0, 0, sum(a)
    a.sort()
    i=1
    while(n>0):
        if(a[n-1]%2==0 and i>0):
            cnt1+=a[n-1]
            sm-=a[n-1]
        elif(a[n-1]%2!=0 and i<0):
            cnt2+=a[n-1]
            sm-=a[n-1]
        n-=1
        i*=-1
        if(abs(cnt2-cnt1)>sm):
            break
    if(cnt1>cnt2): print('Alice')
    elif(cnt2==cnt1): print('Tie')
    else: print('Bob')