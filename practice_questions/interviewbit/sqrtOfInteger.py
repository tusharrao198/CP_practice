import math


def mpow(base, exp):
    mod = 1000000007
    ans = 1
    while exp > 0:
        if exp and 1:
            ans = (ans * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return ans


def sqrt(A):
    return math.floor(math.pow(A, 0.5))


print(sqrt(4))