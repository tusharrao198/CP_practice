from math import ceil

T = int(input())
for t in range(T):
    n = int(input())
    td = []
    for nn in range(n):
        x = list(map(int, input().split()))
        td.append(x)
    tm = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        a, b = td[i]
        extra_time = tm[i]
        if i == 0:
            upper = ceil((b - a) / 2)
            c = a + extra_time
            d = c + upper
            if b > d:
                d = b
        if i > 0:
            extra_time = (td[i][0] - td[i - 1][1]) + tm[i]
            upper = ceil((b - a) / 2)
            c = d + extra_time
            d = c + upper
            if b > d:
                d = b
    print(c)
