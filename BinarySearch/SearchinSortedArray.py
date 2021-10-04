# Serach in a sorted Array


def search(arr, n, target):
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


arr = [1, 2, 3, 6, 8]
n = len(arr)
print(search(arr, n, 2))
