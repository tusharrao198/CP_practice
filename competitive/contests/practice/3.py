n=int(input())
for i in range(n):
    w = input()
    if len(w)>10:
        s = len(w)-2
        x = w[0]+str(s)+w[-1]
        print(x)
    else:
        print(w)
