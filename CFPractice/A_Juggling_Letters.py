tt = int(input())
for _ in range(tt):
    n = int(input())
    lst=[]
    for __ in range(n):
        arr = list(input())
        lst.extend(arr)
    
    mp={}
    for i in lst:
        mp[i]=mp.get(i, 0)+1
    

    for k,v in mp.items():
        if n%2==0 and v%2!=0:
            print("NO")
            break
            
        elif n%2!=0 and v%n!=0:
            # if n is odd then each character frequency should be multiple of n, if not return NO.
            print("NO")
            break
    else:
        print("YES")

