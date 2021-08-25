from math import sqrt, floor, isqrt

tt = int(input())
for _ in range(tt):
    x = int(input())
    n = isqrt(x) ** 2
    while n > 0 and (n & (n - 1) != 0):
        n = isqrt(n - 1) ** 2
    print(n - 1)

tt = int(input())
for _ in range(tt):
    x = int(input())
    c = x
    for i in range(1, x + 1):
        c = c & (x - i)
        if c == 0:
            print(x - i)
            break
