# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def first_num(arr, x):
    l = 0
    r = len(arr) - 1
    mid = 0
    while l <= r:
        mid = (r + l) // 2
        print(f"mid = {mid}")

        if arr[mid] == x:
            if (mid - 1 >= 0) and arr[mid - 1] != x or mid == 0:
                return mid
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
            print(f"l = {l}")
        elif arr[mid] > x:
            r = mid - 1
            print(f"r = {r}")
        print(f"MID = {mid} ")
    return -1


def last_num(arr, x):
    l = 0
    r = len(arr) - 1
    mid = 0
    while l <= r:
        print(f" r = {r} and l = {l}")
        mid = (r + l) // 2
        print(f"mid = {mid}")
        if arr[mid] == x:
            print((mid + 1 <= len(arr) - 1) and arr[mid + 1] != x or mid == len(arr))
            if (mid + 1 <= len(arr) - 1) and arr[mid + 1] != x or mid == len(arr) - 1:
                return mid
            l = mid + 1
        elif arr[mid] < x:
            l = mid + 1
            print(f"l = {l}")
        elif arr[mid] > x:
            r = mid - 1
            print(f"r = {r}")
        print(f"MID = {mid} ")
    return -1


# tt = int(input())
tt = 1
for _ in range(tt):
    n = 8
    res = [5, 7, 7, 8, 8, 8, 3]
    print(res)
    print(first_num(res, n))
    print("\n")
    print(last_num(res, n))
