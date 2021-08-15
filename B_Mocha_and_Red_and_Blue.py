
def solve(arr,x,y):
    for i in range(len(arr)):
        if i%2==0 and arr[i]=="?":
            arr[i] = x
        elif i % 2 != 0 and arr[i] == "?":
            arr[i] = y
    return "".join(arr)

tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = list(input())
    a = solve(lst, "B", "R")
    b = solve(lst, "R", "B")
    ca = 0
    cb = 0
    for i in range(n-1):
        if a[i]==a[i+1]:
            ca+=1
        if b[i] == b[i+1]:
            cb += 1
    if ca<cb:
        print(a)
    else:
        print(b)
