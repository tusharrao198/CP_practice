t = int(input())

def check(small,large,d):
    count = small #1
    new_b = large #6
    if count > 1:
        while (count!=0):
            if new_b>(d+1): 
                new_b -= d+1
            if count ==1:
                break
            elif new_b<(d+1):
                return True
            count -=1
        if count==0:
            return True
    if count == 1:
        if abs(count - large) <= d:
            return True
        else:
            return False

while (t != 0 and t > 0):
    r, b, d = map(int, input().split())
    if d==0:
        if r==b:
            print("YES")
        else:
            print("NO")
    else:
        if r<b and check(r,b,d):
            print("YES")            
        elif r>b and check(b,r,d):
            print("YES")
        else:
            print("NO")
    t-=1
