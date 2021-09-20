from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def countNodesRecurive(root):  # recursive
    if root is None:
        return 0
    return countNodesRecurive(root.left) + countNodesRecurive(root.right) + 1


def SumNodesRecurive(root):  # recursive
    if root is None:
        return 0
    return SumNodesRecurive(root.left) + SumNodesRecurive(root.right) + root.val


def countNodesIterative(root):  # using level order traversal
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)
    # None is pushed to separate out level with none for eg. [10, None, 2, 3, None, 7, 8, 12, 15, None]
    count = 0
    while len(q) > 0:
        node = q.popleft()
        if node != None:
            print(node.val, end=" ")
            count += 1
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        elif len(q) > 0:
            q.append(None)
    print("\n", count)


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


countNodesIterative(root)
print("\ncountNodesRecurive = ", countNodesRecurive(root))
print("\n SumNodesRecurive = ", SumNodesRecurive(root))
print("\n SumNodesIterative = ", SumNodesIterative(root))
