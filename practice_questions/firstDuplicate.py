# in O(n) time and space O(n)
def firstDuplicate(lst):
    track = set()
    for i in range(len(lst)):
        if lst[i] in track:
            return lst[i]
        else:
            track.add(lst[i])
    return -1


# best method
# in O(n) time and space O(1)
# NOTE- given only positive integers
def firstDuplicate1(lst):
    for i in range(len(lst)):
        j = abs(lst[i])-1
        if lst[j] < 0:
            return lst[i]
        else:
            lst[j] = -lst[j]
    return -1


# Time Complexity: O(n)
tt = 1
for _ in range(tt):
    lst = [2, 5, 3, 3, 6]
    print(firstDuplicate1(lst))

