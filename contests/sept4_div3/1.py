# Accepted

n = int(input())
k=[i for i in range(1,11)]
for i in range(n):
    count=0
    a,b =list(map(int,input().split()))
    if a==b:
        count=0
    else:
        diff = abs(b-a)
        if diff>=10:
            times = diff//10
            rem = diff % 10
            count+=times
            if rem in range(1,10):
                count+=1
        else:
            count=1
    print(count)    
            

