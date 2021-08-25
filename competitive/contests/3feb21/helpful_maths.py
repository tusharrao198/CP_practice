s = sorted(input().split("+"))
x = ""
for i in range(len(s)):
    if i < len(s) - 1:
        x += s[i]
        x += "+"
    else:
        x += s[i]
print(x)