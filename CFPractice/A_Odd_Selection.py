tt = int(input())
for _ in range(tt):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    rem=[i%2 for i in arr]
    cntodd=rem.count(1)
    cnteven=n-cntodd 
    aio=0
    for i in range(1, x+1):
        if i%2!=0:
            if cntodd>=i and cnteven>=x-i:
                print("Yes")
                aio=1
                break
    if(aio==0):
        print('No')



# t=int(input())
# for j in range(t):
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     b=[i%2 for i in a]
#     c=b.count(1)
#     if(c==0 or (c==n and k%2==0) or (c%2==0 and n==k)):
#         print("No")
#     else:
#         print("Yes")
 	 		