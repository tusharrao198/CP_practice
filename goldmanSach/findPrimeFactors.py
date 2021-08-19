import math as mt
def prime(n):
    if n==1: return 1
    if n==2: return 2
    if n==3: return 3

    lst = []
    
    while n%2==0:
        lst.append(2)
        n//=2
    
    for i in range(3, int(mt.sqrt(n))+1, 2):
        while n%i==0:
            lst.append(i)
            n//=i
        
    # if n is still greater than 2  then it is a prime number bcoz it will not reach to 1 after these divisions
    if n>2:  lst.append(n)
    return lst

n = 300
print(prime(n))
# for i in range(1, n):
#     print(prime(i))
