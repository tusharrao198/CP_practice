
for _ in range(int(input())):
    n= int(input())
    arr=list(map(int, input().split()))
    target = 2*(sum(arr)/n)

    ans=0
    pos = {}
    for i in range(n):
        if target - arr[i] in pos:
            ans += pos[target - arr[i]]

        if arr[i] in pos:
            pos[arr[i]] += 1
        else:
            pos[arr[i]] = 1
    print(ans)

