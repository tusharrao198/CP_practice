tt = int(input())
for _ in range(tt):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        for j in range(n):
            if i!=j and arr[i]!=0 and arr[j]!=0 and abs(arr[i]-arr[j])<=1:  
                if arr[i]<arr[j]:
                    arr[i]=0
                elif arr[i]>arr[j]:
                    arr[j]=0
                else:
                    arr[i]=0
    
    cnt=0
    for i in range(n):
        if arr[i]!=0:
            cnt+=1
    
    if cnt==1:
        print("YES")
    else:
        print("NO")


            

