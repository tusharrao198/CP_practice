lst=[12,3,43,1,2,23,4]
print(lst.count(2))


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
e, o =getSum(lst)
print(e,o)
print(out(lst))