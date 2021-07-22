n = int(input())
X = 0
for i in range(n):
    x = input()
    
    if '+' in x:
        X+=1
    if "-" in x:
        X-=1
print(X)
