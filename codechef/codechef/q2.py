n = int(input())
for i in range(n):
    count = 0
    a = input().split("0")
    for i in a:
        if len(i) != 0:
            count += 1
    print(count)