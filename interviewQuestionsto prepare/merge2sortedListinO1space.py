# O(1) Space
# O((n+m) log(n+m)) Time
# BEST METHOD

arr2 = [1, 5, 9, 10, 15, 20]
arr1 = [2, 3, 8, 13]

def merge(n, m):
    i = 0
    j = 0
    k = n - 1
    while (i <= k and j < m):
        if (arr1[i] < arr2[j]):
            i += 1
        else:
            arr2[j], arr1[k] = arr1[k], arr2[j]
            j += 1
            k -= 1
        print(arr1, arr2, i, j, k)

    arr1.sort()
    arr2.sort()

merge(len(arr1), len(arr2))
print(arr1, arr2)



# another method

# import math

# def calc_gap(gap):
#     if gap<=1: return 0
#     return math.ceil(gap/2)


# def merge1(arr1, arr2, m, n):
#     gap = m+n
#     gap = calc_gap(gap)

#     while gap>0:
#         print(gap)

#         # for elements in first array arr1
#         i=0
#         while i+gap<m:
#             if arr1[i]> arr1[i+gap]:
#                 arr1[i],  arr1[i+gap] = arr1[i+gap], arr1[i]  
#             i+=1
#             print(gap, i)

#         # compare in both arrays
#         j = 0
#         if gap > m: j = gap-m
#         while i<m and j<n:
#             if arr1[i] > arr2[j]:
#                 arr1[i], arr2[j] = arr2[j], arr1[i]
#             i+=1
#             j+=1

#         if j<n:
#             # if second array elements left
#             j = 0
#             while j+gap < n:
#                 if arr2[j] > arr2[j+gap]:
#                     arr2[j],  arr2[j+gap] = arr2[j+gap], arr2[j]
#                 j += 1

#         gap = calc_gap(gap)
    
# a1 = [3, 27, 38, 43]
# a2 = [9, 10, 82]
# m = len(a1)
# n = len(a2)


# merge(a1, a2, m, n)

# print(a1)
# print(a2)

        


            





        


