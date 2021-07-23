# Binary Tree Node
class newNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.hd = 0


def printNodesAtLevelOfTree(root):
    if not root: return
    q = [root]
    count = 1
    level_nodes = [[1, q[0].val]]
    while len(q):
        count += 1
        n = len(q)  # number of nodes at current level
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
            if temp.left is not None: q.append(temp.left)
            if temp.right is not None: q.append(temp.right)
        if len(q) != 0:
            level_nodes.append([count, [i.val for i in q]])
    return level_nodes


if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    print(printNodesAtLevelOfTree(root))


