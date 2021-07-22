tt = int(input())
for _ in range(tt):
    s = input()
    # n = len(s)
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    fx, fy = map(int, input().split())
    res = abs(ax - bx) + abs(ay - by)
    if ax == bx and ax == fx and (ay < fy < by or by < fy < ay):
        res += 2
    if ay == by and ay == fy and (ax < fx < bx or bx < fx < ax):
        res += 2
    print(res)
