import sys
from math import ceil, log2

MAX_SIZE = sys.maxsize


def getMid(a, b):
    return (a + b) // 2


def getMin(a, b):
    return min(a, b)


def buildTreeMain(tree, arr, low, high, pos):
    if low == high:
        tree[pos] = arr[low]
        # print(arr[low])
        return arr[low]
    mid = getMid(low, high)
    tree[pos] = buildTreeMain(tree, arr, low, mid, (2 * pos + 1)) + buildTreeMain(tree, arr, mid + 1, high,
                                                                                  (2 * pos + 2))
    return tree[pos]


def buildTree(arr, n):
    height = int(ceil(log2(n)))
    max_size = 2 * int(2 ** height) - 1
    tree = [0] * max_size
    buildTreeMain(tree, arr, 0, n - 1, 0)
    return tree


def rangeSumMain(tree, low, high, qs, qe, pos):
    # print(low, high, pos)
    if qs <= low and qe >= high:
        # print(pos, tree[pos])
        return tree[pos]
    if high < qs or low > qe:
        # print("return 0")
        return 0
    mid = getMid(low, high)
    sum_ = rangeSumMain(tree, low, mid, qs, qe, 2 * pos + 1) + rangeSumMain(tree, mid + 1, high, qs, qe, 2 * pos + 2)
    # print("S", sum_)
    return sum_


def rangeSum(tree, n, qs, qe):
    if qs < 0 or qe > n - 1 or qs > qe:
        return "INVALID INPUT"
    return rangeSumMain(tree, 0, n - 1, qs, qe, 0)


def updateValMain(tree, low, high, index, diff, pos):
    # Base Case: If the input index lies
    # outside the range of this segment
    if index < low or index > high:
        return

    # If the input index is in range of this node,
    # then update the value of the node and its children
    tree[pos] += diff

    if low != high:
        mid = getMid(low, high)
        updateValMain(tree, low, mid, index, diff, 2 * pos + 1)
        updateValMain(tree, mid + 1, high, index, diff, 2 * pos + 2)


def updateVal(tree, arr, n, index, new_val):
    if index < 0 or index > n - 1:
        return "INVALID INDEX"
    diff = new_val - arr[index]
    arr[index] = new_val
    updateValMain(tree, 0, n - 1, index, diff, 0)
    return


def main():
    arr = [11, 2, 4, -1]
    print(f"arr = {arr}")
    n = len(arr)
    segment_tree = buildTree(arr, n)
    print(f"segment_tree before = {segment_tree}")
    print(f"sum = {rangeSum(segment_tree, n, 2, 2)}")
    index, new_val = 0, -1
    updateVal(segment_tree, arr, n, index, new_val)
    print(f"arr after = {arr}")
    print(f"segment_tree after = {segment_tree}")
    print(f"sum after = {rangeSum(segment_tree, n, 2, 3)}")


main()
