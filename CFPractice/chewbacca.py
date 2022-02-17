arr = [int(_) for _ in list(input())]
a=""
for i in reversed(arr):
    if i>(9-i):
        a+=str(9-i)
    else:
        a+=str(i)

if int(a[-1])==0:
    a=a[:-1]+"9"
ans=int(a[::-1])
print(ans)
