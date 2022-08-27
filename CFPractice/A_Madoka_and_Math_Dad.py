import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())    
    if n==1:
        print(1)
    elif n==2:
        print(2)
    else:
        arr = []
        sum_ = 0
        i=0
        while sum_<n:
            if i%2==0:
                arr.append(2)
                sum_+=2
            else:
                arr.append(1)
                sum_+=1 
            i+=1
        
        if sum_==n+1:
            final = []

            for i in arr:
                if i==2:
                    final.append(1)
                else:
                    final.append(2)
            for i in final:
                print(i,end="")
            print()

        elif sum_==n:
            for i in arr:
                print(i,end="")
            print()
        
