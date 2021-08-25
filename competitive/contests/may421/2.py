# # # def single(inp_):
# # #     watch = "123"
# # #     inp_ = [int(_) for _ in str(inp_)]

# # #     while (len(watch)!=1):
# # #         watch = str(sum(inp_))
# # #         print(watch)
# # #         if watch in range(0,10):
# # #             print("YES")
# # #         else:
# # #             continue
# # #     return watch



# # import math
# # def single( n):
# # 	sum = 0
# # 	while(n > 0 or sum > 9):
# # 		if(n == 0):
# # 			n = sum
# # 			sum = 0
# # 		sum += n % 10
# # 		n /= 10
# # 	return math.floor(sum)

# # print(single(1060))

# def prime_(s , e):
#     lst =[]
#     for i in range(s,e+1):
#         if i>1:
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 lst.append(i)
#     return sum(lst)

# print(prime_(2,22))

# a = [i*3 for i in range(150)]
# b = (i*3 for i in range(150))

# print(a[0:5:-2])
# print(b[0:5:-2])


# dd = [[]]*5
# print(dd)


# def Compute(prog):
#     def ComputeInside(*args, **kwargs):
#         return prog(*args, **kwargs)+1
#     return ComputeInside
# @Compute

# def result(n):
#     return n-4
# print(result(5))


# def Task(p, i):
#     i=iter(i)
#     for x in i:
#         if not p(x):
#             yield x
#             break
#     for x in i:
#         yield x
# a = Task(lambda x: x<5, [4,-2,0,1,3,-1,10,33])

# for i in range(2):
#     print(next(a), end=' ')

from collections import Counter as cc

def chars(s1,s2):
    d1 = cc(s1)
    d2 = cc(s2)

    d = d1&d2
    if len(d) ==0:
        return 0
    chars = list(d.elements())
    chars = sorted(chars)
    return ''.join(chars)

print(chars('Python', 'HackerEarth'))