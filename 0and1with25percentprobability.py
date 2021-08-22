import random

# generate 0 with 25% probability and 75 % prob 1 

def rand50():
    return int(10*(random.random())) & 1

def random_genrator():
    return rand50() | rand50()

arr = []
for i in range(10000):
    arr.append(random_genrator())

print((arr.count(1)/len(arr))*100) # 1's with 75 % probability
