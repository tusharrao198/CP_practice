import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    n= int(inp())
    arr=list(map(int, inp().split()))
    arr.sort()

    # first found min_difference b/w neighbours for the start and end of the cliff
    # max difficulty can be n-2
    min_diff = float("inf")
    l = 0
    r = 0
    for i in range(n-1):
        x = abs(arr[i]-arr[i+1])
        if x<min_diff:
            min_diff = x
            l = i
            r = i+1            
    # print(l, r)
    ans = [arr[l]]
    
    ans.extend(arr[r+1:])
    ans.extend(arr[:l])
    ans.append(arr[r])
    
    for i in ans:
        print(i, end=" ")
    print()




