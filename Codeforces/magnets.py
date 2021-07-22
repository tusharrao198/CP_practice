# n = int(input())
# count = 1
# b = input()  
# for i in range(n-1):
#     a = input()
#     if a != b:
#         count+=1
#         b=a
# print(count)

n = int(input())
count = 0
b = ""
for i in range(n):
    a = input()
    b += a
print(b)
lst = b.split("00")




