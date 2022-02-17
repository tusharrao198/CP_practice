# def prod(a):
#     ans = 1
#     for i in a:
#         ans*=i
#     return ans

# for _ in range(int(input())):
#     n= int(input())
#     arr=list(map(int, input().split()))
#     arr.sort(reverse=True, key=lambda x: abs(x))

#     if max(arr)<0:
#         print(prod(arr[-5:]))
#         continue

#     # print(arr)
#     ans = prod(arr[:5])
#     for i in range(5,n):
#         for j in range(5):
#             tmp = arr[i]
#             for k in range(5):
#                 if k!=j:
#                     tmp*=arr[k]
#             ans = max(ans, tmp)
#     print(ans)



################ -----   Second Approach   ------ ###################

for _ in range(int(input())):
    n= int(input())
    a=list(map(int, input().split()))
    a.sort()

    x = a[-5]*a[-1]*a[-2]*a[-3]*a[-4]
    
    y = a[0]*a[1]*a[2]*a[3]*a[4]
    
    z = a[0]*a[1]*a[-1]*a[-2]*a[-3]

    w = a[0]*a[1]*a[2]*a[3]*a[-1]

    print(max(x,y,z,w))
