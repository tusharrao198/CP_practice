import math

t = int(input())
if t in range(1, 101):
    for tt in range(1, t + 1):
        n, k = list(map(int, input().split()))
        if k>=0 and k <=n/2:
            a = list(input())
            count = 0
            for i in range(math.floor(len(a) / 2)):
                if a[i] != a[len(a) - (i + 1)]:
                    count += 1
            print(f"Case #{tt}: {abs(count-k)}")