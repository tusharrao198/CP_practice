import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    # cnt = k//n
    # while cnt>0:
    #     if (k+1)%n!=0:
    #         cnt-=1
    #     k+=1
    # print(k)
    
    ans = k + math.floor((k - 1) / (n - 1))
    print(ans)