tc = int(input())
record = 9.58
for t in range(tc):
    k1, k2, k3, v = list(map(float, input().split()))
    c_speed = 100/(k1*k2*k3*v) 
    if round(c_speed, 2) < record:
        print("YES")
    else:
        print("NO")
