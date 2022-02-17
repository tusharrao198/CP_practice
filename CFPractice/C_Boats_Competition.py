tt = int(input())
for _ in range(tt):
    n = int(input())
    arr=list(map(int, input().split()))

    cnt = [0] *(n+1)

    for i in range(n):
        cnt[arr[i]]+=1
    
    ans = 0
    for i in range(2, 2*n+1):
        cur = 0
        for j in range(1, (i+1)//2):
            if (i-j)>n:
                continue
            cur = cur + min(cnt[j], cnt[i-j])

        if i%2==0:
            cur=cur + (cnt[i//2]//2)
        ans = max(ans, cur)
    
    print(ans)
