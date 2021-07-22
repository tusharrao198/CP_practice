mod = 10 ** 9 + 7


def solve(A):
    lastTwo = [0, 1]
    counter = 3
    while counter <= A:
        nextFib = (lastTwo[0] + lastTwo[1]) % mod
        lastTwo[0] = lastTwo[1] % mod
        lastTwo[1] = nextFib % mod
        counter += 1
        # print(12 % mod)
    return lastTwo[1] % mod if A > 1 else (lastTwo[0]) % mod


print(solve(40) % mod)
