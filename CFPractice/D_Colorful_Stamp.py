import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    ss = input()
    w = 0
    r = 0
    b= 0
    boll_val = False
    for i in range(n):
        if ss[i]=="W":
            if (r==0 and b>0) or (b==0 and r>0) :
                print("NO")
                boll_val=True
                break
            else:
                r=0
                b=0
                        
        elif ss[i]=="R":
            r+=1
        else:
            b+=1

    if boll_val:
        continue
    if(r==0 and b>0) or (b==0 and r>0):
        print("NO")
    else:
        print("YES") 
    

    
