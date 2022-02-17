n= int(input())
arr=list(map(int, input().split()))
m= int(input())
lst=list(map(int, input().split()))

ll = []
cnt = 0
for i in arr:
    cnt+=1
    for j in range(i):
        ll.append(cnt)

for i in lst:
    print(ll[i-1])