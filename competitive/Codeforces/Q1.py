t = int(input())
lst11=[]
if t in range(1,11):
    for t in range(t):
        dict={}
        lst=[]
        lstd=[]
        n = int(input())
        if n in range(1,1001):
            for i in range(n):
                sf = input()
                if len(sf) in range(1,1001):
                    lst.append(sf)
            a = ""
            ss = a.join(lst)
            lstd = list(ss)
            for k in lstd:
                dict[k] = dict.get(k,0)+1
            
            lsteven = list(dict.values())
            count=0
            for sd in lsteven:
                if sd%2==0:
                    count+=1
                else:
                    continue
            if count==len(lsteven) and sum(lsteven)<1000:
                lst11.append("YES")

            else:
                lst11.append("NO")
for h in lst11:
    print(h)    

