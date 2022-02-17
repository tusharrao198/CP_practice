for _ in range(int(input())):
    n= int(input())
    arr=list(map(int, input().split()))
    
    # if n==1 return that elem
    if n==1:
        print(arr[0])
        continue
    
    # if all negative then return max elem
    # if all positive then return max elem
    cntneg = 0
    cntpos = 0
    mx = arr[0]
    for i in range(n):
        if arr[i]>0:
            cntpos+=1
        elif arr[i]<0:
            cntneg+=1
        mx = max(mx, arr[i]) 

    if cntneg==n or cntpos==n:
        print(mx)    
        continue 

    a = [arr[0]]
    # r = 0
    mx=arr[0]
    for i in range(1, n):
        if arr[i-1]>0:
            if arr[i]>0:
                # a[r].append(arr[i])
                mx=max(mx,arr[i])

            elif arr[i]<0:
                # a[r].append(mx)
                a.append(mx)
                # a.append([arr[i]])
                # r+=1
                mx=arr[i]

            if i==n-1:
                # a[r].append(mx)
                a.append(mx)

        elif arr[i-1]<0:
            if arr[i]>0:
                # a[r].append(mx)
                a.append(mx)
                # a.append([arr[i]])
                # r+=1
                mx=arr[i]

            elif arr[i]<0:
                # print("AS", arr[i], a)
                # a[r].append(arr[i])
                mx=max(mx,arr[i])
            
            if i==n-1:
                # a[r].append(mx)
                a.append(mx)
    # print(a[1:])
    ans = []
    for i in range(len(a)-1):
        ans.append(a[i+1])
    print(sum(ans))