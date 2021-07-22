
n,k ,x = list(map(int, input().split()))
lst = sorted(list(map(int, input().split())))
print(lst)
store=[]
for i in range(1, len(lst)):
    print(f'lst[i] = {lst[i]} and lst[i-1] => {lst[i-1]}')
    ans = lst[i]-lst[i-1]
    if abs(ans)>x:
        if k>0 and (ans)%k==0:
            lst.insert((ans)//k, i)
            k-=1
        else:
            store.append(i)
    print("NOW=> ", lst)
print(store, len(store))
        
        


