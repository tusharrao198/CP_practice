from math import comb
# https://www.geeksforgeeks.org/count-triplets-such-that-one-of-the-numbers-can-be-written-as-sum-of-the-other-two/


def countingTriplets(arr, n):
    max_val = max(arr)
    count = 0
    f = {}  # frequency
    for i in range(max_val + 1):
        f[i] = 0
    for i in arr:
        f[i] = f.get(i, 0) + 1

    # if a == 0 and b == 0:
    count += comb(f[0], 3)  # nC3

    # elif a == 0 or b == 0:
    # 0 + x = x
    for i in range(1, max_val + 1):
        count += comb(f[0], 1) * comb(f[i], 2)

    # elif a == b: a + a = 2*a
    j = 0
    while j >= 1 and 2 * j <= max_val + 1:
        count += comb(f[j], 2) * comb(f[2 * j], 2)
        j += 1

    # elif a != b:
    # a + b = c
    for i in range(1, max_val + 1):
        for j in range(i + 1, max_val - i + 1):
            # print(i, j)
            count += (comb(f[i], 1) * comb(f[j], 1) * comb(f[i + j], 1))

    return count


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(countingTriplets(arr, n))
