for _ in range(int(input())):
    n= int(input())
    a=list(map(int, input().split()))
    found = False

    for i in range(0, n-1):
        if abs(a[i+1]- a[i])>1:
            print("YES")
            print(i+1, i+2)
            found=True
            break

    if not found:
        print("NO")
    