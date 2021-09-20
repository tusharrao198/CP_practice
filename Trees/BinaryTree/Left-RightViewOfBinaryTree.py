from collections import deque

# Binary Tree Node
class newNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def leftViewMain(root, max_level, level):
    if root is None:
        return
    if max_level[0] < level:
        print(root.val)
        max_level[0] = level

    # switch these recursive calls for left view(keep left up), and for right view(keep root.right) up
    leftViewMain(root.left, max_level, level + 1)
    leftViewMain(root.right, max_level, level + 1)


def leftView(root):
    max_level = [0]
    leftViewMain(root, max_level, 1)


def printLeftView(root):
    if root is None:
        return

    q = deque()
    q.append(root)

    while len(q) > 0:
        n = len(q)
        for i in range(1, n + 1):
            node = q.popleft()
            if i == 1:  # i = 1 for left view and n for right view
                print(node.val)

            if node.left != None:
                q.append(node.left)

            if node.right != None:
                q.append(node.right)


root = newNode(10)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(7)
root.left.right = newNode(8)
root.right.right = newNode(15)
root.right.left = newNode(12)
root.right.right.left = newNode(14)
leftView(root)
# printLeftView(root)
