s = input()
# s = "There are 2 cats and 12 kit10s"
count = 0
alpha = []
for i in range(1, len(s)):
    if s[i].isalpha() and s[i-1].isnumeric():
        alpha+= s[i]+ " "   
        count+=1
    else:
        continue
print(f"{''.join(alpha)}\n{count}")
