import math

test = int(input())
for i in range(test):
    n = int(input())
    lst = list(map(int, input().split()))
    kk = []
    count = -1
    if len(lst) % 2 != 0:
        for k in range(int(len(lst) / 2) + 1):
            try:
                kk.append(lst[k])
                if k != int(len(lst) / 2):
                    kk.append(lst[count])
                    count -= 1
            except:
                break
    else:
        for k in range(int(len(lst) / 2)):
            try:
                kk.append(lst[k])
                kk.append(lst[count])
                count -= 1
            except:
                break
    for aa in kk:
        print(aa, end=" ")