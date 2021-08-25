t = int(input())

def fun(t):
    a, b, c = list(map(int, input().split()))
    count=1
    count1=1
    if a==0 or b==0 or c==0:
        return "NO"
    if c==0:
        return "NO"
    
    if c==1:
        return "YES"

    if a%2==0 and b%2!=0:
        while a%2==0 and a!=0:
            a=a/2
            count+=2
        if count >=c:
            return "YES"

    if a%2!=0 and b%2==0:
        while b%2==0 and b!=0:
            b=b/2
            count1+=2
        if count1 >=c:
            return "YES"

    if a%2==0 and b%2==0:
        while a%2==0 and a!=0:
            a=a/2
            count+=2
        
        while b%2==0 and b!=0:
            b=b/2
            count1+=2

        if count+count1 >=c:
            return "YES"
    if a%2!=0 and b%2!=0 and c==1: 
        return "YES"
    else:
        return "NO"


for i in range(t):
    print(fun(t))



