tt = int(input())

def get11s(num, len_):
    a = ''.join(['1' for o in range(len_)]) #111
    res = int(a)
    if (num < res):
        res = int(a[:-1]) 
    return res






for _ in range(tt):
    ds = False
    n = input()
    num = int(n)  
    res = get11s(num, len(n))
    
    while (num>=11 and num>=res):
        num = num%res
        print("NUM => ",num)
        if (num%res==0):
            ds = True
            break
        res = get11s(num, len(str(num)))
    if ds:
        print("YES")
    else:
        print("NO")

