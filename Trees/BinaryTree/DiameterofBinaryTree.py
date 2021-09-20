from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# O(n) time  , n= no. of  nodes
# without height function

# utility class
class Height:
    def __init__(self) -> None:
        self.h = 0


# -----------------------------------------------------------------------------------------------------------
#  O(n) approach
def calcDiameterMain(root, height):
    lh = Height()
    rh = Height()
    if root is None:
        height.h = 0
        return 0
    ldiam = calcDiameterMain(root.left, lh)
    rdiam = calcDiameterMain(root.right, rh)

    # a function call reaches at this point after calculating rdiam, ldiam , that means
    # for each node whose left subtree and right subtree is traversed, we now have the height of that subtree
    # stored in lh.h and rh.h now we just need to calculate the height using
    # height.h = max(lh.h, rh.h) + 1

    # print(root.val, lh.h, rh.h)
    currDiam = lh.h + rh.h + 1  # diameter at this node
    height.h = max(lh.h, rh.h) + 1

    return max(currDiam, max(ldiam, rdiam))


def calcDiameter(root):
    height = Height()
    return calcDiameterMain(root, height)


# -------------------------------------------------------------------------------------------------------------


def heightRecurcive(root):  # recursive
    if root is None:
        return 0

    l = heightRecurcive(root.left)
    r = heightRecurcive(root.right)
    return max(l, r) + 1


# O(n**2) time  calling height function inside calDiamter n times
def calDiameterOn2(root):
    if root is None:
        return 0

    lh = heightRecurcive(root.left)
    rh = heightRecurcive(root.right)
    currDiam = lh + rh + 1

    ldiam = calDiameterOn2(root.left)
    rdiam = calDiameterOn2(root.right)

    return max(currDiam, max(ldiam, rdiam))


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

# print(calDiameterOn2(root))
print(calcDiameter(root))
