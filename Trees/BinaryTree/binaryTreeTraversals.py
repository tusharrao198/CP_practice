
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

# left => root => right
def inOrderTraversal(node):
    if node is not None:
        inOrderTraversal(node.left)
        print(node.data, end= " ")
        inOrderTraversal(node.right)

# root => left => right
def preOrderTraversal(node):
    if node is not None:
        print(node.data,end=" ")
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

# left => right => root
def postOrderTraversal(node):
    if node is not None:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node.data, end=" ")


    #               4
    #         /        \
    #         5          6
    #     /     \      /   \
    #    7     None   None  None
    # /     \
    # None  None


root = Node(4);
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

print(" In-Order Traversal")
# In-Order Traversal
# left -> root -> right
# print(root.data)
inOrderTraversal(root)

print("\n\n\n# Pre-Order Traversal")
# Pre-Order Traversal
preOrderTraversal(root)
# root -> left -> right
print("\n")

print("\n\n # postOrderTraversal")
# postOrderTraversal
# left -> right -> root
postOrderTraversal(root)
print("\n")





