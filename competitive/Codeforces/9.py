t = input()
d = input()
ls = list(t)
s = "".join(ls[::-1])
if s==d:
    print("YES")
else:
    print("NO")