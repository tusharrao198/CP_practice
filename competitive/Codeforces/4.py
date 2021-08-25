a, b = list(map(int, input().split()))
for i in range(b):
    if str(a)[-1]=='0':
        a=a//10
    else:
        a-=1
print(a)