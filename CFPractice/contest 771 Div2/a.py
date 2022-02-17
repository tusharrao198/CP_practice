for _ in range(int(input())):
    n= int(input())
    arr=list(map(int, input().split()))
    l = 0
    r= n-1
    while l<=r:
        if arr[l]>arr[r]:

            ans = []
            for i in reversed(range(l,r+1)):
                ans.append(arr[i])

            if r+1<n:
                ans.extend(arr[r+1:])
            print(ans)
            break
        else:
            r-=1


