# t = int(input())
# for tt in range(1, t + 1):
#     n, b = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     a = sorted(a)
#     left = b
#     count = 0
#     for i in range(len(a)):
#         if a[i] < b and left >= a[i]:
#             left -= a[i]
#             count += 1

#     print(f"Case #{tt}: {count}")

# or using count sort

t = int(input())


def count_sort(input_array, r):
    count = []
    lsto = []
    for l in range(len(input_array)):
        lsto.append(0)
    for i in range(r + 1):
        count.append(0)
    for j in input_array:
        count[j] += 1
    for m in range(1, len(count)):
        count[m] += count[m - 1]
    for k in input_array:
        indexo = count[k] - 1
        count[k] = indexo
        lsto[indexo] = k
    return lsto


for tt in range(1, t + 1):
    n, b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = count_sort(a, max(a))
    left = b
    count = 0
    for i in range(len(a)):
        if a[i] < b and left >= a[i]:
            left -= a[i]
            count += 1

    print(f"Case #{tt}: {count}")
