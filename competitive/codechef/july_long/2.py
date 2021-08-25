tt = int(input())
for _ in range(tt):
    g, c = map(int, input().split())
    print(c ** 2 // (2 * g))
