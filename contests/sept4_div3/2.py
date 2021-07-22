t = int(input())
for i in range(t):
    count=0
    a,b,x,y,n =list(map(int,input().split()))
    if a==x and b==y:
        print(a*b)
    if a==b and a==x and b==y:
        print(a*b)
    if a==b and a>x and b>y:
        diff_a = a-x
        diff_b = b-y
        for same in range(n):
            
            if diff_a > diff_b:
                if a!=x:
                    a-=1
                    count+=1
                if a==x and b>y:
                    b-=1
                    count+=1
                if count==n:
                    break
            else:
                if b!=y:
                    b-=1
                    count+=1
                if b==y and a>x:
                    a-=1
                    count+=1
                print(count)
                if count==n:
                    break
        
            
    elif a!=b:
        diff_a = a-x
        diff_b = b-y
        for same in range(n):
            if diff_a > diff_b:
                if a>b:
                    if b>y:
                        b-=1
                        count+=1
                    if b==y and a>x:
                        a-=1
                        count+=1
                    if count==n:
                        break
                if a<b:
                    if a>x:
                        a-=1
                        count+=1
                    if a==x and b>y:
                        b-=1
                        count+=1
                    if count==n:
                        break

            if diff_a < diff_b:
                if a<b:
                    if a>x:
                        a-=1
                        count+=1
                    if a==x and b>y:
                        b-=1
                        count+=1
                    if count==n:
                        break
                if a>b:
                    if b>y:
                        b-=1
                        count+=1
                    if b==y and a>x:
                        a-=1
                        count+=1
                    if count==n:
                        break
                

                
    print(a*b)
            
