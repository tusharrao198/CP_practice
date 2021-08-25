t = int(input())
count=0
for i in range(t):
    p = 2
    a, b = list(map(int, input().split()))
    if (b-a)>=2:
        count+=1
print(count)
