n = input()
a = int(n)
b = int(n)

while (int(n)>=1000 and int(n)<=9000):
    if a>int(n) and len(set(list(str(a))))==len(n):
        print(a)
        break
    else:
        a+=1
