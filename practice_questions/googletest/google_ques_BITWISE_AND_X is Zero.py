# where bitwise AND X is zero


n=int(input())
a=set([int(i) for i in input().split()])
store=set()

def all_possible_comb(a):

    # if already in store, then return
    if tuple(a) in store:
        return

    # if length of a == 0, then add it to store and return
    if len(a)==0:
        store.add(tuple(a))
        return

    # add a to the store
    store.add(tuple(a))

    # recursion
    for i in range(len(a)):
        all_possible_comb(a[:i]+a[i+1:])


## main function
for i in a:
    x=i
    zero_bits=[]
    ind=0

    for ind in range(17):
        if x%2==0:
            zero_bits.append(ind)
        x//=2
    all_possible_comb(zero_bits)

# queries
for query in range(int(input())):
    k=int(input())
    one_bits=[]

    for ind in range(17):
        if k%2==1:
            one_bits.append(ind)
        k//=2
    
    if tuple(one_bits) in store:
        print("Yes")
    else:
        print("No")


