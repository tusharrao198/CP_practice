# https://www.geeksforgeeks.org/sum-of-subtree-depths-for-every-node-of-a-given-binary-tree/

global h


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


# sum of all depths of given tree
def depth(root, h):
    if root is None:
        return 0

    l = depth(root.left, h + 1)
    r = depth(root.right, h + 1)

    ht = h + l + r
    return ht


# sum of all depths of given tree  and it's subtrees
def sumofAllSubtreesdepth(root, h):
    p = [1, 0]

    # print("MAIN ", root.val, h, p )
    if root.left is not None:
        # print("L ", root.left.val,p, h)
        ptemp = sumofAllSubtreesdepth(root.left, h)
        # print("root.left ", root.val, "->",root.left.val, p , ptemp, h)

        p[1] += ptemp[0] + ptemp[1]

        p[0] += ptemp[0]

    if root.right is not None:
        # print("R ", root.right.val, p, h)
        ptemp = sumofAllSubtreesdepth(root.right, h)
        # print("root.right ", root.val, "->", root.right.val,p,  ptemp, h)

        p[1] += ptemp[0] + ptemp[1]

        p[0] += ptemp[0]

    h[0] += p[1]

    return p


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)


h = [0]
# print(depth(root, 0))
print(sumofAllSubtreesdepth(root, h))
print(h[0])
