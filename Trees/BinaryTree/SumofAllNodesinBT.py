from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


# in O(n) time  and O(n) space


def SumNodesRecurive1(root):  # recursive
    if root is None:
        return 0
    return SumNodesRecurive(root.left) + SumNodesRecurive(root.right) + root.val


def SumNodesRecurive(root, s):  # recursive
    if root is None:
        return 0
    s[0] += root.val
    SumNodesRecurive(root.left, s)
    SumNodesRecurive(root.right, s)
    print(root.val, s)


def SumNodesIterative(root):  # using level order traversal
    if root is None:
        return 0
    q = deque()
    q.append(root)
    sum_ = 0
    while len(q) > 0:
        node = q.popleft()
        sum_ += node.val
        if node.left != None:
            q.append(node.left)

        if node.right != None:
            q.append(node.right)

    # print(sum_)
    return sum_


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

# print("\n SumNodesRecurive = ", SumNodesRecurive(root))
print("\n SumNodesIterative = ", SumNodesIterative(root))

s = [0]
SumNodesRecurive(root, s)
print(s)
