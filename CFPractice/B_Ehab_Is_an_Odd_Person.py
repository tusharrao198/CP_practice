
n= int(input())
arr=list(map(int, input().split()))
cnt0=0
cnt1=0
for i in arr:
    if i%2==0:
        cnt0+=1
    else:
        cnt1+=1
if cnt0 and cnt1:
    arr.sort()
for i in arr:
    print(i, end=" ")