for _ in range(int(input())):
    n= int(input())
    arr=list(map(int, input().split()))
    
    l = 0
    r = 0

    for i in range(n):
        if arr[i]!=i+1:
            l=i
            break
    
    for i in range(n):
        if arr[i]==l+1:
            r = i

    ans = []
    tmp = []
    for i in range(l):
        tmp.append(arr[i])

    for i in reversed(range(l,r+1)):
        ans.append(arr[i])

    tmp.extend(ans)
    
    for i in range(r+1, n):
        tmp.append(arr[i])


    if n==1:
        print(arr[0])
    else:
        for i in tmp:
            print(i, end=" ")
        print()
