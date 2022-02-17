
tt = int(input())
for _ in range(tt):
    a, b = map(int, input().split())
    if a==1:
        print(b)
    else:
        x=0
        y=0
        for i in range(b+1, 20):
            # print("l",i)
            lst = [int(_) for _ in list(str(i))]
            y=sum(lst)
            if y==b:
                # print(i)
                y=i
                break
        d = y-b

        ans= b+(d*(a-1))
        print(ans)

