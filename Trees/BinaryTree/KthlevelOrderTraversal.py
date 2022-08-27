from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def levelOrder(root): # not complete
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)


def levelOrder1(root, k):
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)
    # None is pushed to separate out level with none for eg. [10, None, 2, 3, None, 7, 8, 12, 15, None]
    sum_ = 0
    # level = 1 # if root is considered as level 1
    level = 0  # root level as 0
    while len(q) > 0:
        node = q.popleft()
        if node != None:
            if level == k:
                print([node.val, level], end=" ")
                sum_ += node.val
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        elif len(q) > 0:
            level += 1  
            q.append(None)
    print("\n", sum_)


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

levelOrder1(root, 2)
