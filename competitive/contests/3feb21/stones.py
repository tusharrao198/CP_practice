n = int(input())
a = list(input())
c = 0
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        c += 1
        break
    else:
        c += 0
print(c)
