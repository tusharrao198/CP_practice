t = int(input())
lst1=[]
if t in range(1,1001):
    for i in range(t):
        n = int(input())
        if n in range(1,1001):
            lst = list(map(int, input().split()))
            if n==1 or n%2!=0:
                lst1.append("T")
            elif n%2==0:
                lst1.append("HL")
for h in lst1:
    print(h)
            


