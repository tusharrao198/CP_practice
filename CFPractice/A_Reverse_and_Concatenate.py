tt = int(input())
for _ in range(tt):
    n, k = map(int, input().split())
    s=input()
    rs=s[::-1]
    if k==0:
        print(1)
    elif rs==s:
        print(1)
    else:
        print(2)
