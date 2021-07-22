# # rabbit
# import math
# import numpy as np

# t = int(input())
# if t in range(1, 101):
#     for tt in range(1, t + 1):
#         r, c = list(map(int, input().split()))
#         if r >= 1 and r <= 300 and c >= 1 and c <= 300:
#             lst = sorted(list(map(int, input().split())), reverse=True)
#             for k in range(len(lst)):
#                 if lst[k]


#                 # count = 0
#                 # for i in range(math.floor(len(a) / 2)):
#                 #     if a[i] != a[len(a) - (i + 1)]:
#                 #         count += 1
#                 # print(f"Case #{tt}: {abs(count-k)}")

l = [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
row = len(l) - 1
col = len(l[0]) - 1
a, b = []
for r in range(len(l)):
    for c in range(len(l[0])):
        if l[r][c] != 0:
            a = r
            b = c
x = []
if a < row and b < col and a == b and a == row / 2 and b == col / 2:
    x.append([a + 1, b])
    x.append([a, b + 1])
    x.append([a, b - 1])
    x.append([a - 1, b])

if a < row and b < col and b == 0:
    x.append([a + 1, b])
    x.append([a, b + 1])
    x.append([a - 1, b])

if a < row and b < col and a == 0:
    x.append([a + 1, b])
    x.append([a, b + 1])
    x.append([a - 1, b])
