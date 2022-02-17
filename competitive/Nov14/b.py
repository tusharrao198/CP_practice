t=int(input())

for _ in range(t):
    a, b = map(int, input().split())
    x = a*b
    c = x//3
    d = x%3
    if d!=0:
        print(c+1)
    else:
        print(c)