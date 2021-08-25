tt = int(input())
for _ in range(tt):
    n = int(input())

    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a)
    tot = 0
    count = 0
    for i in a:
        tot+=i
        if tot<0:
            break
        count+=1
    print(count)
