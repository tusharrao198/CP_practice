tt = int(input())
for _ in range(tt):
    n, k = map(int, input().split())
    # print(n, k)
    if (n-k)>=0 and (n-k)%2==0: # then odd are possible
        ans = []
        s = 0
        for i in range(k-1):
            ans.append(1)
            s+=1
        if (n-s)%2!=0:
            print("YES")
            ans.append(n-s)
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()    

    elif (n-2*k)>=0 and (n-2*k)%2==0: # then even are possible 
        ans = []
        s = 0
        for i in range(k-1):
            ans.append(2)
            s+=2
        if (n-s)%2==0:
            print("YES")
            ans.append(n-s)
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()
    else:
        print("NO")