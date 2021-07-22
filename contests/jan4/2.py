t = int(input())

def fun(t):
    sum_ = int(input())
    ss = list(map(int, input().split()))
    if len(ss)%2==0:
        if sum(ss)%2==0:
            ce=0
            aaa=ss[0]
            same_e=0 
            for e in ss:
                
                if e%2==0:
                    ce+=1
                if aaa==e:
                    same_e+=1
            if same_e==len(ss):
                return "YES"

            if ce==len(ss):
                return "YES"
            else:
                return "NO"

        else:
            sd=0
            asdf=ss[0]
            same_o=0
            for k in ss:
                if k%2==0:
                    sd+=1
                if asdf==k:
                    same_o+=1
            if same_o==len(ss):
                return "YES"

            if sd==len(ss):
                return "YES"
            else:
                return "NO"

    # if len is odd
    else:
        if sum(ss)%2!=0:
            co = 0
            aq =ss[0]
            sm=0
            for o in ss:
                if o%2==0:
                    co+=1
                if aq==o:
                    sm+=1
            if sm==len(ss):
                return "YES"

            if co==len(ss):
                return "YES"
            else:
                return "NO"
        else:
            sf=0
            xx=ss[0]
            x=0
            for h in ss:
                if h%2==0:
                    sf+=1
                if xx==h:
                    x+=1
            if x==len(ss):
                return "YES"
                
            if sf==len(ss):
                return "YES"
            else:
                return "NO"

for i in range(t):
    print(fun(t))
