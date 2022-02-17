tt = int(input())
for _ in range(tt):
    n, m = map(int, input().split())
    mul = set()
    lst = []

    for i in range(1, 11):
        v= (i*m)%10
        if v in mul:
            break
        else:            
            mul.add(v)
            lst.append(v)
    sm = sum(lst)
    # 100 3
    # x = 33
    x = n//m
    c = x%len(lst)

    ans = ((x-c)//len(lst)) * sm
    for i in range(c):
        ans+=lst[i]
    print(ans)

    


# 2 4 6 8 0 = 20
# 3 9 2 5 8 1 4 7 0  = 39
# 4 8 2 6 0 = 20
# 5 0       = 5
# 6 2 8 4 0 = 20
# 7 4 1 8 5 2 9 6 3 0 = 45
# 8 6 4 2 0 = 20
# 9 8 7 6 5 4 3 2 1 0 = 45