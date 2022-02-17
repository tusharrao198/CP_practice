
tt = int(input())
for _ in range(tt):
    n,m,r,c = map(int, input().split())
    mat=[]
    cntw=0
    for i in range(n):
        abc=list(input())
        for j in range(m):
            if abc[j]=="W":
                cntw+=1
        mat.append(abc)

    if cntw==(n*m):
        print(-1)
    
    elif mat[r-1][c-1]=="B":
        print(0)

    else:
        rsame=False 
        csame=False       
        for k in range(n):
            for l in range(m):
                if mat[k][l]=="B":
                    if k==r-1:
                        rsame=True
                        break   
                    if l==c-1:
                        csame=True
                        break
        if rsame or csame:
            print(1)
        else:
            print(2)

    
            