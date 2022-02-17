# for _ in range(int(input())):
from math import ceil, floor
from turtle import left
n= int(input())
arr=list(map(int, input().split()))
arr=list(set(arr))
x = len(arr)

mn = min(arr)
mx = max(arr)
if x>3:
    print(-1)
    
elif x==3:
    leftout = 0
    for i in range(3):
        if arr[i]==mn or arr[i]==mx:
            continue
        else:
            leftout = i
    
    if abs(mx-arr[leftout])==abs(mn-arr[leftout]):
        print(abs(mx-arr[leftout]))
    else:
        print(-1)


elif x==2:
    avg = sum(arr)/x
    if ceil(avg)!=floor(avg):
        print(abs(arr[0]-arr[1]))
    else:
        ans=mx - int(avg)
        print(ans)

elif x==1:
    print(0)

