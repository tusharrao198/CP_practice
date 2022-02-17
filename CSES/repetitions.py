l=input()
a=1
mx=1
for i in range(1,len(l)):
    if l[i-1]==l[i]:
        a+=1
    else:
        a=1
    mx=max(mx, a)
print(mx)

