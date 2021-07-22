tot = 0
count = 0
nn = int(input())
lst = list(map(int, input().split()))
a = sorted(lst, reverse=True)
print(a)
for i in a:
    tot += i
    print()
    if tot < 0:
        break
    count += 1
print(count)
