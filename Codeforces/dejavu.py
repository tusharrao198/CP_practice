t = int(input())

def check(s):
    l = len(s)
    if l%2!=0:
        mido = (l+1)//2
        ll = s[:mido]
        lo = s[mido-1:]
        lo = lo[::-1]
        # print(ll, lo)
        if ll == lo:
            return True
        else:
            return False

    else:
        mide = (l+1)//2
        l1 = s[:mide]
        l2 = s[mide : ]
        l2 = l2[::-1]
        # print(l1, l2)
        if l1==l2:
            return True
        else:
            return False

while (t != 0 and t > 0):
    s = input()
    if s=="a":
        print("NO")
    elif len(set(s)) == 1 and list(set(s))[0]=="a":
        print("NO")
    else:    
        cc="a"+s
        if check(cc):
            s+="a"
            print("YES")
            print(s)
        
        else:
            s = cc
            print("YES")
            print(s)
    t-=1
