t = int(input())
while (t!=0 and t>0):
    n , k = map(int, input().split())
    if n<=2*k:
        arr = -1
        print(arr)
    else:
        arr = [i for i in range(1, n+1)]
        for i in range(k):
            arr[-(2 * i + 1)], arr[-(2 * i + 2)] = arr[-(2 * i + 2)], arr[-(2 * i + 1)]
        print(*arr)
    t-=1