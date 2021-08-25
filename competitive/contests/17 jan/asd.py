
t = int(input())

one=0
two=0
lead=0
for i in range(t):
    a, b = list(map(int, input().split()))
    one+=a
    two+=b 

if abs(two-one)>=0:
    lead = abs(two-one)
max=0
if one>two:
    max=1 
else:
    max=2
print(max, lead)
    

        