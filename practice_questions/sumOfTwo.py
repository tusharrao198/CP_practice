def sumOfTwo(lst1, lst2, target):
    diff = set()
    for i in lst1:
        diff.add(target-i)

    for i in lst2:
        if i in diff:
            return True
    return False


# tt = int(input())
tt = 1
for _ in range(tt):
    # lst1 = list(map(int, input().split()))
    # lst2 = list(map(int, input().split()))
    lst1 = [0,0,-5,302]
    lst2 = [-10,40,-3,22]
    # target = int(input())
    target = -8
    if sumOfTwo(lst1, lst2, target):
        print("TRUE")
    else:
        print("FALSE")
