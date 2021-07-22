t = int(input())

def getSum(lst):   
    sumOdd = 0
    sumEven = 0
    for i in range(len(lst)):
        if ((i+1) % 2 == 0): 
            sumEven +=lst[i]
        elif ((i+1)%2!=0):
            sumOdd+= lst[i]
    return sumEven , sumOdd
def out(lst):
    lste=[]
    lsto=[]
    for i in range(len(lst)):
        if ((i+1) % 2 == 0):
            lste.append(lst[i])
        elif ((i+1)%2!=0):
            lsto.append(lst[i])
    return lste, lsto

for i in range(t):
    lst = map(int, input().split())
    e, o=out(lst)
    se, so=getSum(lst)
    count =0
    if sum(se)==sum(so):
            print(len(lst))
            print(lst)
            break
        
            
