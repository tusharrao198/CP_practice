tt = int(input())
for _ in range(tt):
    d,x,y,z = map(int, input().split())
    print(max(7*x , ((d*y)+ (z*(7-d)))))