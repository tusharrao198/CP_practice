from itertools import accumulate
n= int(input())
arr=list(map(int, input().split()))

m= int(input())
a=sorted(arr)
b= [i for i in accumulate(a)]
c= [i for i in accumulate(arr)]

for i in range(m):
    type, l, r = map(int, input().split())
    l = l-1
    r= r-1
    if type==2:
        print(b[r]-b[l]+a[l])
    else:
        print(c[r]-c[l]+arr[l])
