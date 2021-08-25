tt = int(input())


def solve(n, x, y, a, b):
    if x > n and y > n:
        return False

    if x == n or y == n:
        print("IF ", x, y)
        return True

    else:
        print(x, y)
        if solve(n, x * a, y, a, b) or solve(n, x, y + b, a, b):
            return True

    return False


for _ in range(tt):
    n, a, b = map(int, input().split())
    # cur = set()
    x = 1
    y = 1
    print(solve(n, x, y, a, b))
