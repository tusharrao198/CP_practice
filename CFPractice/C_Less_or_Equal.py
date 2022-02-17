
n, k= map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
if n<k:
    print(-1)
elif k==0:
    if arr[0]==1:
        print(-1)
    elif arr[0]>1:
        print(1)

else:
    dd = dict()
    for i in arr:
        dd[i] = dd.get(i,0) + 1

    cnt = 0
    l = 0
    arr = list(set(arr))
    # print(arr)
    while k>0:
        # print(k, l)
        if dd[arr[l]]==1:
            k-=1
        elif dd[arr[l]]>1:
            k-=dd[arr[l]]
        if k>0:
            l+=1
    # print("k = ", k, l)
    if k<0:
        print(-1)
    else:
        ans = arr[l]
        print(min(10**9, ans))
            
            