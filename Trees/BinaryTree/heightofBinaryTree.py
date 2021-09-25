class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# O(n) time  , n= no. of  nodes
def heightRecurcive(root):  # recursive
    if root is None:
        return 0

    l = heightRecurcive(root.left)
    r = heightRecurcive(root.right)
    return max(l, r) + 1


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

print("\n heightRecurcive = ", heightRecurcive(root))
