class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


global s
s = [0]


def leaf(root, s):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.val, end=" -> ")
        s[0] += root.val
        return

    leaf(root.left, s)
    leaf(root.right, s)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(7)
root.right.left = Node(6)
root.right.left.right = Node(8)

print(leaf(root, s))
print(s)
