# tz, h, x = list(map(int, input().split()))
# tz_s = list(map(int, input().split()))

from itertools import permutations as pm

# n = int(input())
# for i in range(n):
#     zz = int(input())
#     a = bin(zz)[2:]
# perm = pm(a)
# x = [int("".join(_), 2) for _ in perm]
# x = list(set(x))
# print(x)
# # for i in range(len(x)):
# c = [10]
for i in range(16):
    for j in range(16):
        if i ^ j == zz:
            # print(x[i] * c[j])
            print(i * j)

# print(int("1001", 2))
