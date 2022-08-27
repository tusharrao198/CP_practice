import sys
inp = sys.stdin.readline
for _ in range(int(inp())):
    s = inp()
    lst = []
    count_ = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            lst.append(count_+1)
            count_=0
        else:
            count_+=1
    for i in lst:
        if i==1:
            print("NO")
            break
    else:
        print("YES")