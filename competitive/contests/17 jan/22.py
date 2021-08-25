def fun(arr1, arr2, n1, n2, arr3) :
    i = 0; j = 0; k = 0
    while (i < n1 and j < n2) :
        arr3[k] = arr1[i]
        i += 1
        k += 1

        arr3[k] = arr2[j]
        j += 1
        k += 1
    while (i < n1) :
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while (j < n2) :
        arr3[k] = arr2[j]
        k += 1
        j += 1

t = int(input())
def main():
    lst3 = []
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    n1 = len(arr1)

    n2 = len(arr2)

    arr3= [0] *(n1 + n2)
    fun(arr1, arr2, n1, n2, arr3)

    for i in range(0, (n1 + n2)) :
        lst3.append(arr3[i])
    return lst3

def rec(lst3):
    ans=0
    sum=0
    for el in range(len(lst3)):
        sum+=lst3[el]
        ans = max(ans,sum)
    return ans

for i in range(t):
    print(rec(main()))

