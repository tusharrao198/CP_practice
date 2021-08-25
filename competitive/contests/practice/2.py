n = int(input())
count=0
for i in range(n):
    a,b,c = list(map(int , input().split()))
    if (a+b+c)>=2:
        count+=1
    else:
        continue
print(count)
