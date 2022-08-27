import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    l, r,a = map(int, inp().split())

    if r%a==(a-1):
        print((r//a)+(a-1))
    else:
        if (r-a>=l):
            ans = ((((r//a)*a)-1)//a)+(a-1)
            print(ans)

        elif ((l%a)>(r%a)):
            ans = ((((r//a)*a)-1)//a)+(a-1)
            print(ans)

        else:
            print((r//a)+(r%a))