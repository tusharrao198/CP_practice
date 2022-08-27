import sys
inp = sys.stdin.readline

n=int(inp())
s = inp()
cnt = 0
for i in range(1,n):
    if s[i]==s[i-1]:
        cnt+=1
print(cnt)