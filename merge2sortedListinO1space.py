import math

def calc_gap(gap):
    if gap<=1: return 0
    return math.ceil(gap/2)


def merge(arr1, arr2, m, n):
    gap = m+n
    gap = calc_gap(gap)

    while gap>0:
        print(gap)

        # for elements in first array arr1
        i=0
        while i+gap<m:
            if arr1[i]> arr1[i+gap]:
                arr1[i],  arr1[i+gap] = arr1[i+gap], arr1[i]  
            i+=1
            print(gap, i)

        # compare in both arrays
        j = 0
        if gap > m: j = gap-m
        while i<m and j<n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i+=1
            j+=1

        if j<n:
            # if second array elements left
            j = 0
            while j+gap < n:
                if arr2[j] > arr2[j+gap]:
                    arr2[j],  arr2[j+gap] = arr2[j+gap], arr2[j]
                j += 1

        gap = calc_gap(gap)
    
a1 = [3, 27, 38, 43]
a2 = [9, 10, 82]
m = len(a1)
n = len(a2)


merge(a1, a2, m, n)

print(a1)
print(a2)

        


            





        


