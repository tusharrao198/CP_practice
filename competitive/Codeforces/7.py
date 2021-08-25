t = input()
lower = 0
upper = 0
for i in t:
    if i.islower():
        lower+=1
    if i.isupper():
        upper+=1

if lower == upper:
    print(t.lower())
elif upper>lower:
    print(t.upper())
else:
    print(t.lower())
