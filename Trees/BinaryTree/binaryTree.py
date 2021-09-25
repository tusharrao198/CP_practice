# Queue using Linked List


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print(custQueue.peek())
# print(custQueue)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinaryTree:
    def levelOrderTraversal(self, root):
        if root is None:
            return

        q = Queue()
        q.enqueue(root)

        while not q.isEmpty():
            root = q.dequeue()
            print(root.value.val)

            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)

    def searchNode(self, root, key):
        if root is None:
            return

        q = Queue()
        q.enqueue(root)

        while not q.isEmpty():
            root = q.dequeue()
            if root.value.val == key:
                return True

            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)

        return False

    def insertNode(self, root, newnode):
        if root is None:
            return

        q = Queue()
        q.enqueue(root)

        while not q.isEmpty():
            root = q.dequeue()

            if root.value.left is None:
                root.value.left = newnode
                print("newnode inserted as left child of ", root.value.val)
                return "INSERTED L"
            else:
                q.enqueue(root.value.left)

            if root.value.right is None:
                root.value.right = newnode
                print("newnode inserted as right child of ", root.value.val)
                return "INSERTED R"
            else:
                q.enqueue(root.value.right)

    def getDeepestNode(self, root):
        if root is None:
            return

        q = Queue()
        q.enqueue(root)

        while not q.isEmpty():
            root = q.dequeue()

            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)

        return root.value

    def deleteNode(self, root, deletenode):
        if root is None:
            return

        deepestNode = self.getDeepestNode(root)
        # if deepestNode is None: return

        q = Queue()
        q.enqueue(root)

        while not q.isEmpty():
            root = q.dequeue()

            if root.value.val == deletenode:
                root.value, deepestNode = deepestNode, root.value
                deepestNode = None
                return "SUCCESS DELETE"

            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)


root = TreeNode("Drinks")
left = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
left.left = tea
left.right = coffee
right = TreeNode("Cold")
root.left = left
root.right = right

bt = BinaryTree()
# bt.levelOrderTraversal(root)
# print(bt.searchNode(root, "Coffee"))

newnode = TreeNode("CHAI")
print(bt.insertNode(root, newnode))
print("---------------------")
bt.levelOrderTraversal(root)
print("---------------------")
print(bt.getDeepestNode(root).val)
print(bt.deleteNode(root, "Coffee"))
print("---------------------")
bt.levelOrderTraversal(root)
