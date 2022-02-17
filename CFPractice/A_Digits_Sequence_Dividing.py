
tt = int(input())
for _ in range(tt):
    x=int(input())
    a=input()
    if x==2 and int(a[0])>=int(a[1]):
        print("NO")
    else:
        print("YES")
        print(2)
        print(int(a[0]), int(a[1:]))
