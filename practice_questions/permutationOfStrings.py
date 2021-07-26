def swap(s, i, j):
    # print(s, i, j )
    temp = s[j]
    s[j] = s[i]
    s[i] = temp
    return


def permutationOfStrings(s, l, r):
    if l <= r:
        if l == r:
            lst.append("".join(s))
            # print(s)
            # return s
        else:
            for i in range(l, r + 1):
                swap(s, l, i)
                permutationOfStrings(s, l + 1, r)
                swap(s, l, i)
    return


def permutationOfStrings1(s, l, r):
    if l <= r:
        if l == r:
            lst.append("".join(s))
            # print(s)
            # return s
        else:
            for i in range(l, r + 1):
                s[l], s[i] = s[i], s[l]  # swap
                permutationOfStrings(s, l + 1, r)
                s[l], s[i] = s[i], s[l]
    return

# tt = int(input())
tt = 1
for _ in range(tt):
    global lst
    lst = []
    str1 = list("AB")
    permutationOfStrings(str1, 0, len(str1) - 1)
    print(len(lst))
    print(lst[:])
