import sys

rd = sys.stdin.readline
t = int(rd())
for _ in range(t):
    n = int(rd())
    a = [list(list(rd().strip())) for _ in range(n)]
    pair = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == "*":
                pair.append([i, j])
    x1 = pair[0][0]
    x2 = pair[1][0]
    y1 = pair[0][1]
    y2 = pair[1][1]

    # if rows equal
    if x1 == x2:
        if (x1 + 1) <= n - 1:
            a[x1 + 1][y1] = "*"
            a[x2 + 1][y2] = "*"
        elif (x1 - 1) >= 0:
            a[x1 - 1][y1] = "*"
            a[x2 - 1][y2] = "*"

    if y1 == y2:  # if columns equal
        if (y1 + 1) <= n - 1:
            a[x1][y1 + 1] = "*"
            a[x2][y1 + 1] = "*"
        elif (y1 - 1) >= 0:
            a[x1][y1 - 1] = "*"
            a[x2][y1 - 1] = "*"

    else:
        a[x1][y2] = "*"
        a[x2][y1] = "*"

    for __ in a:
        print("".join(__))

# 1
# 4
# ..*.
# ....
# *...
# ....
