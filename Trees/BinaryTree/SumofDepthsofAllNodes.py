from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depthSum(root):
    if root is None:
        return 0

    q = deque()
    q.append(root)
    q.append(None)
    level = 0
    dsum = 0

    while len(q) > 0:
        node = q.popleft()
        if node is not None:
            dsum += level

            if node.left != None:
                q.append(node.left)

            if node.right != None:
                q.append(node.right)

        elif len(q) > 0:
            q.append(None)
            level += 1

    return dsum


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

print(depthSum(root))
