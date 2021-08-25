tt = int(input())
for _ in range(tt):
    n = int(input())
    nums = list(map(int, input().split()))
    ce = 0
    co = 0
    for i in nums:
        if i % 2 == 0:
            ce += 1
        else:
            co += 1
    if co == ce:
        print("Yes")
    else:
        print("No")


# tt = int(input())


# def solve(nums, ans, cur, index):
#     if len(cur) == 2:
#         if sum(cur) % 2 == 1:
#             ans.append(cur[:])
#         else:
#             return
#     else:
#         for i in range(index, len(nums)):
#             if len(cur) < 2:
#                 cur.append(nums[i])
#                 solve(nums, ans, cur, i + 1)

#                 cur.pop()
#     return


# for _ in range(tt):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     ans, cur = [], []
#     nums.sort()
#     solve(nums, ans, cur, index=0)
#     print("pairs ", ans)
#     count = 0
#     check = set()
#     for i in range(len(ans)):
#         if ans[i][0] not in check and ans[i][1] not in check:
#             check.add(ans[i][0])
#             check.add(ans[i][1])
#             count += 1
#     print("count ", count)
#     if count == n:
#         print("Yes")
#     else:
#         print("No")
