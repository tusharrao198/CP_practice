def solve(n, lst):
    count = 0
    for i in range(n):
        if lst[i]!=0:
            lst[count] = lst[i]
            count+=1    
    for i in range(count, n):
        lst[i]= 0

tt = int(input())
for _ in range(tt):
    # n, k = map(int, input().split())
    # res = map(int, input().split())
    n = 5
    res = [0 ,1,0,3,12]
    solve(n, res)
    print(res)
