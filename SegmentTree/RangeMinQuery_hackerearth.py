import sys
from math import ceil, log2

MAX_SIZE = sys.maxsize


def getMid(a, b):
    return (a + b) // 2


def buildTreeMain(tree, arr, low, high, pos):
    if low == high:
        tree[pos] = arr[low]
        # print(arr[low])
        return arr[low]
    mid = getMid(low, high)
    tree[pos] = min(buildTreeMain(tree, arr, low, mid, (2 * pos + 1)),
                    buildTreeMain(tree, arr, mid + 1, high, 2 * pos + 2))

    return tree[pos]


def buildTree(arr, n):
    height = int(ceil(log2(n)))
    max_size = 2 * int(2 ** height) - 1
    tree = [0] * max_size
    buildTreeMain(tree, arr, 0, n - 1, 0)
    return tree


def updateValMain(tree, low, high, index, new_val, pos):
    if low == high:
        tree[pos] = new_val
    else:
        mid = getMid(low, high)
        if low <= index <= mid:
            updateValMain(tree, low, mid, index, new_val, 2*pos+1)
        else:
            updateValMain(tree, mid + 1, high, index, new_val, 2 * pos + 2)
        tree[pos] = min(tree[2*pos+1], tree[2*pos+2])
    return


def updateVal(tree, arr, n, index, new_val):
    if index < 0 or index > n - 1:
        return "INVALID INDEX"
    arr[index] = new_val
    updateValMain(tree, 0, n - 1, index, new_val, 0)


def rangeMinMain(tree, low, high, qs, qe, pos):
    if qs <= low and qe >= high:
        return tree[pos]
    # If segment of this node
    # is outside the given range
    if high < qs or low > qe:
        return MAX_SIZE
    # If a part of this segment
    # overlaps with the given range
    mid = getMid(low, high)
    return min(rangeMinMain(tree, low, mid, qs, qe, 2 * pos + 1),
               rangeMinMain(tree, mid + 1, high, qs, qe, 2 * pos + 2))


def rangeMin(tree, n, qs, qe):
    if qs < 0 or qe > n - 1 or qs > qe:
        return "INVALID INPUT"
    return rangeMinMain(tree, 0, n - 1, qs, qe, 0)

#
# def main():
#     # arr = [11, 2, 4, -1]
#     arr = [1, 5, 2, 4, 3]
#     print(f"arr = {arr}")
#     n = len(arr)
#     segment_tree = buildTree(arr, n)
#     print(f"segment_tree before = {segment_tree}")
#     print(f"Min before = {rangeMin(segment_tree, n, 0, 4)}")
#     print(f"Min before = {rangeMin(segment_tree, n, 0, 2)}")
#     print(f"Min before = {rangeMin(segment_tree, n, 2, 4)}")
#     updateVal(segment_tree, arr, n, 3, 6)
#     print(f"Min before = {rangeMin(segment_tree, n, 0, 4)}")

    # index, new_val = 0, -1
    # updateVal(segment_tree, arr, n, index, new_val)
    # print(f"arr after = {arr}")
    # print(f"segment_tree after = {segment_tree}")
    # print(f"Min after = {rangeMin(segment_tree, n, 2, 3)}")


def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    segtree = buildTree(arr, n)

    for i in range(q):
        q, a, b = map(str, input().split())
        a = int(a)
        b = int(b)
        if q == "q":
            print(rangeMin(segtree, n, qs=a-1, qe=b-1))
        elif q == "u":
            updateVal(segtree, arr, n, a, b)


main()
