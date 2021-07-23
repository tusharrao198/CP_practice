# Python3 program to print left view of
# Binary Tree

# Binary Tree Node
class newNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.hd = 0


# function to print left view of
# binary tree


def printRightView(root):
    if not root: return
    q = [root]
    while len(q):
        # number of nodes at current level
        n = len(q)
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)

            # Print the left most element
            # at the level
            if i == 1:
                print(temp.val, end=" ")

            # Add left node to queue
            if temp.left != None:
                q.append(temp.left)

            # Add right node to queue
            if temp.right != None:
                q.append(temp.right)


# Driver Code
if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    printRightView(root)

# This code is contributed by
# Manne SreeCharan
