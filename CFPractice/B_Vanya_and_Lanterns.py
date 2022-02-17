n, a = map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()

mx = -1
for i in range(1, n):
    mx = max(mx, arr[i]-arr[i-1])

print(max(float(arr[0]-0), float(a - arr[-1]), float(mx/2)))