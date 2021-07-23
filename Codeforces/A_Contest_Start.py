tt = int(input())
for _ in range(tt):
    n,x ,t = list(map(int, input().split()))
    lsti = [] 
    lstf= []
    c = 0
    lsti.append(0)
    for i in range(n-1):
        c+=x
        lsti.append(c)
    # end_= t
    # lstf.append(end_)
    for j in range(n):
        cc = lsti[j]+t
        lstf.append(cc)
    # print(lsti, lstf)
    count=0
    for k in range(n):
        for l in range(k+1, n):
            if lsti[l] <=lstf[k]:
                count +=1
    print(count)        