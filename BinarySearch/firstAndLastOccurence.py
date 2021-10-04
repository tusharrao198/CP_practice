# given sorted Array
def firstOccurence(arr, target):
    n = len(arr)
    l, r = 0, n - 1

    ans_index = -1
    while l <= r:
        # print(l, r)
        mid = l + (r - l) // 2
        if arr[mid] == target:
            # print(mid, arr[mid])
            ans_index = mid
            r = mid - 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return arr[ans_index], ans_index


def lastOccurence(arr, target):
    n = len(arr)
    l, r = 0, n - 1

    ans_index = -1
    while l <= r:
        # print(l, r)
        mid = l + (r - l) // 2
        if arr[mid] == target:
            # print(mid, arr[mid])
            ans_index = mid
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return arr[ans_index], ans_index


arr = [1, 2, 10, 10, 10, 23, 25, 63]
print(firstOccurence(arr, 10))
print(lastOccurence(arr, 10))
