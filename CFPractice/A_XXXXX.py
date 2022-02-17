tt = int(input())
for _ in range(tt):
    n, x = map(int, input().split())
    arr=list(map(int, input().split()))
    rem = [i%x for i in arr]
    # 1 2 0
    # 0 5000 5000 0 0
    cnt=0
    for i in arr: # if every element is divisible by x then print(-1)
        if i%x==0:
            cnt+=1
    if cnt==n:
        print(-1)
    else:
        l = 0
        r = n-1
        sm = sum(rem)
        sm1=sm
        ans=-1
        # print(n,x)
        while sm%x==0 and l<=n-1:
            sm-=rem[l]
            l+=1

        ans=r-l+1
        # print("ans = ", l,r,ans)
        l = 0
        r = n-1
        ans1=-1
        while sm1%x==0 and r>=0:
            sm1-=rem[r]
            r-=1
        
        ans1= r-l+1
        # print("ans1 = ", l,r,ans1)
        b = max(ans1,ans)
        print(b)
