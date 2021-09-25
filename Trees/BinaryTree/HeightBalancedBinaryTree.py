class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1


def heightBalanced(root):

    if root == None:
        return True

    if not heightBalanced(root.left):
        return False
    if not heightBalanced(root.right):
        return False

    lh = height(root.left)
    rh = height(root.right)

    if abs(rh - lh) <= 1:
        return True
    return False


# --------------------------------------
# O(n) approach
class Height:
    def __init__(self) -> None:
        self.h = 0


def heightBalanced1Main(root, height):
    lh = Height()
    rh = Height()

    if root == None:
        return True

    if not heightBalanced1Main(root.left, lh):
        return False

    if not heightBalanced1Main(root.right, rh):
        return False

    height.h = max(lh.h, rh.h) + 1

    print(root.val, height.h, lh.h, rh.h)
    if abs(rh.h - lh.h) <= 1:
        return True
    return False


def heightBalanced1(root):
    height = Height()
    return heightBalanced1Main(root, height)


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)
root.right.right.left.left = Node(1)


print(heightBalanced1(root))
