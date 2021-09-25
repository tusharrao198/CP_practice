# Binary Tree Node
class newNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def LCA(root, n1, n2):
    if root == None:
        return None

    if root.val == n1 or root.val == n2:
        return root

    l = LCA(root.left, n1, n2)
    r = LCA(root.right, n1, n2)

    if l == None and r == None:
        return None

    if l != None and r != None:
        return root

    if l != None:
        return LCA(root.left, n1, n2)

    if r != None:
        return LCA(root.right, n1, n2)


def distanceBw2NodesMain(root, key, dist):
    if root == None:
        return -1

    if root.val == key:
        return dist

    l = distanceBw2NodesMain(root.left, key, dist + 1)
    if l != -1:
        return l

    return distanceBw2NodesMain(root.right, key, dist + 1)


def distance(root, n1, n2):
    lca = LCA(root, n1, n2)
    d1 = distanceBw2NodesMain(lca, n1, 0)
    d2 = distanceBw2NodesMain(lca, n2, 0)
    return d1 + d2


def main(root):
    return distance(root, 14, 7)


root = newNode(10)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(7)
root.left.right = newNode(8)
root.right.right = newNode(15)
root.right.left = newNode(12)
root.right.right.left = newNode(14)

print(main(root))
