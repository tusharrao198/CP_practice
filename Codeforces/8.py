t = input()
n = [int(_) for _ in t]
count_both = 0
for i in range(len(n)):
    if n[i] == 7 or n[i] == 4:
        count_both+=1
if count_both==7 or count_both==4:
    print("YES")
else:
    print("NO")

