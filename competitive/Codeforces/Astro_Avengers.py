import math
n,k = list(map(int, input().split()))
lst = sorted(list(map(int, input().split())), reverse=True)
mod = 10**9 + 7
count =0
while (k>0):
    lst.pop(0)
    k-=1
    count+=1

def solve(res):
    cc = 1
    ans = res
    while True:
        if ans==2:
            # cc+=2
            break
        if ans==3:
            # cc+=3
            break
        if ans!=res:
            cc+= ans*math.floor(math.sqrt(ans))
        else:
            cc+= math.floor(math.sqrt(ans))
        cc= cc%mod
        # print("CC ", cc)
        ans = math.floor(math.sqrt(ans))
        # print("ANS ", ans)
    return cc%mod


for i in range(len(lst)):
    count+= solve(lst[i])
    count = count %mod
    

print(count)