# replace all the nodes with sum of al nodes of its subtree

from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# O(n) time  , n= no. of  nodes
# without sum_ function

# utility class
class Sum:
    def __init__(self) -> None:
        self.h = 0


# -----------------------------------------------------------------------------------------------------------
#  O(n) approach
def sumReplaceMain(root, sum_):
    lsum = Sum()
    rsum = Sum()
    if root is None:
        sum_.h = 0
        return 0

    sumReplaceMain(root.left, lsum)
    sumReplaceMain(root.right, rsum)
    # print(root.val, lsum.h, rsum.h)
    sum_.h = lsum.h + rsum.h + root.val
    root.val = sum_.h


def sumReplace(root):
    sum_ = Sum()
    sumReplaceMain(root, sum_)


# --------------------------------------------------------
# Another approach
# O(n)
def sumReplace1(root):
    if root is None:
        return

    sumReplace1(root.left)
    sumReplace1(root.right)

    if root.left != None:
        root.val += root.left.val

    if root.right != None:
        root.val += root.right.val


# ---------------------------------------------------------

# left => root => right
def inOrderTraversal(node):
    if node is not None:
        inOrderTraversal(node.left)
        print(node.val, end=" ")
        inOrderTraversal(node.right)


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

inOrderTraversal(root)
sumReplace1(root)
print("\n")
inOrderTraversal(root)
