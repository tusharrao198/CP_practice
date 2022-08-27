# O(n*m)
def merge2A(arr1, arr2, l1, l2):

    for i in range(l2-1, -1, -1):
        last = arr1[l1-1]
        j = l1-2
        while (j>=0 and arr1[j] > arr2[i]):
            arr1[j+1] = arr1[j]
            j-=1

        if last>arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last

    return arr1+arr2

arr1 = [1,5,9,10,15,20]
arr2 = [2,3,8,13]
m1, n2 = len(arr1), len(arr2)
x = merge2A(arr1, arr2, m1, n2)

print(x)