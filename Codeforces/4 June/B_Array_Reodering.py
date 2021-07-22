import math

tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))
    count = 0
    x = range(len(lst))
    for i in x:
        for j in range(i + 1, len(lst)):
            if (math.gcd(lst[i], 2 * lst[j]) > 1) or (math.gcd(2 * lst[i], lst[j]) > 1):
                count += 1
    print(count)
