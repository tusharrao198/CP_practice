t = int(input())
for kk in range(t):
    n, k = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    b = 0
    count = k  
    while (count>0 and b<(n-1)):
        if lst[b]>0:
            lst[b] -= 1
            lst[-1]+=1
            count-=1
        elif lst[b]==0:
            b+=1
    print(" ".join(map(str, lst)))