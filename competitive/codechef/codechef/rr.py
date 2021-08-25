# ques 1
# n = int(input())
# a = list(map(int, input().split()))
# lst = []
# count = 0
# for i in range(len(a) - 1):
#     if a[i] < a[i + 1]:
#         count += 1
#         lst.append(count + 1)
#     else:
#         count = 0
# print(max(lst))


# ques 2
# n = int(input())
# tree = list(input())
# for i in range(len(tree)):
#     if tree[i] != "a" and tree[i] != "h":
#         tree[i] = "x"
# jj = "".join(tree)
# cc = jj.split("x")
# count = 0
# for k in cc:
#     for j in range(len(k) - 1):
#         if (k[j] == "a" and k[j + 1] == "h") or (k[j] == "h" and k[j + 1] == "a"):
#             count += 1
#         else:
#             count = 0
# print(count + 1)
