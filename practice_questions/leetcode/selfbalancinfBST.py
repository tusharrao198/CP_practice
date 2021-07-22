from bisect import bisect_left, bisect_right
# track = []

# https: // www.geeksforgeeks.org/largest-element-smaller-than-current-element-on-left-for-every-element-in-array/

def find_lt(a, x):
    # 'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return i-1
    return -1


# def solve(arr, num):
#     track = []
#     track.append(arr[0])

#     for i in range(1,len(arr)-1):
#         res = find_lt(arr, num)
#         track.insert(res+1, arr[i])
#         print(track)
#     return track[res]

# def findMaximumBefore(arr, n, num):

#     # Self Balancing BST
#     s = set()
#     for i in range(n):
#         if i==0 and arr[i]==num: # no element at left side of first element 
#             return -1
#         elif arr[i]==num:
#             res = find_lt(list(s), num)
#             return arr[res]
#         # Insertion in BST
#         s.add(arr[i])
#         print(f"s1 = {s}")
#         # Lower Bound the element arr[i]
#         s.add(arr[i] * 2)
#         print(f"s2 = {s}")
#     return list(s)


# arr = [2, 5, 3, 6, 1, 4, 1]
# print(findMaximumBefore(arr, len(arr), 6))
