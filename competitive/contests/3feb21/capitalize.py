s = list(input())
x = ""
for i in range(len(s)):
    if i == 0:
        x += s[0].upper()
    else:
        x += s[i]
print(x)