tt = int(input())
for _ in range(tt):
    n,x,y = map(int, input().split())
    arr=list(map(int, input().split()))
    ali=x
    bo=x+3
    for i in range(n):
        ali+=arr[i]
        bo+=arr[i]
    if ali%2==0 and y%2==0:
        print("Alice")
    elif ali%2!=0 and y%2!=0:
        print("Alice")
    else:
        print("Bob")
        
