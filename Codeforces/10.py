n = int(input())
t = input()

ca = 0
cd = 0

for i in t:
    if i=="A":
        ca+=1
    if i=="D":
        cd+=1
if ca==cd:
    print("Friendship")
if ca>cd:
    print("Anton")
if ca<cd:
    print('Danik')
