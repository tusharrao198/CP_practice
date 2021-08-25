def shift(lst):
    arr = []
    if len(lst) % 2 != 0:
        i = 0
        while i < n:
            if i == n - 1:
                temp = str(arr[i - 1])
                arr[i - 1] = str(lst[i])
                arr.append(temp)
            else:
                arr.append(str(lst[i + 1]))
                arr.append(str(lst[i]))

            i += 2
        return " ".join(arr)

    else:
        i = 0
        while i < n:
            arr.append(str(lst[i + 1]))
            arr.append(str(lst[i]))
            i += 2
        return " ".join(arr)


tt = int(input())
for _ in range(tt):
    n = int(input())
    lst = [_ for _ in range(1, n + 1)]
    print(shift(lst))
