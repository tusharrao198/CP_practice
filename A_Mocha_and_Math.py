tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(map(int, input().split()))
    for i in range(n//2):
        lst[i] = (lst[i]& lst[n-i-1])
        lst[n-i-1] = (lst[i] & lst[n-i-1])
    print(min(lst))