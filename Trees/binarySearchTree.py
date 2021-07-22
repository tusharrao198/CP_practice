class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

class BST:

    def insert(self, root, node):
        if root is None:
            root = node
            return

        if node.data > root.data:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

        if node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)


    def preOrderTraversal(self, node):
        if node is not None:
            print(node.data, end =" ")
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)


    def searchNode(self, node, key):  
        # key is value of node to be searched
        print(f"search current Node is -> {node.data}")
        if node is None:
            print("Not Found")
            return None
        if node.data==key:
            return node
        if node.data < key:
            return self.searchNode(node.right, key)
        if  node.data > key:
            return self.searchNode(node.left, key)

    def deleteNode(self, node , key):
        print(f"delete current Node is -> {node.data}")
        if node is None:
            return None
        if node.data > key:
            node.left = self.deleteNode(node.left, key)
        elif node.data < key:
            node.right = self.deleteNode(node.right, key)
        # if node.data == key:
        else:
            # if node has one child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            # else if node has 2 childs then,
            temp = self.minimumValue(node.right) # finding the minimum value in the right subtree
            print("t = ", temp.data)
            node.data = temp.data
            print(f"node.right = {node.right.data}")
            node.right = self.deleteNode(node.right, temp.data)

        return node


    def minimumValue(self, node):
        while node.left is not None:
            node = node.left
        return node

        
node = Node(5)
tree = BST()

tree.insert(node, Node(3))
tree.insert(node, Node(2))
tree.insert(node, Node(4))
tree.insert(node, Node(7))
tree.insert(node, Node(6))
tree.insert(node, Node(8))

tree.preOrderTraversal(node)
# root -> left -> right
print()

# x = tree.searchNode(node, 6)
# print(x.data)

print(tree.deleteNode(node, 7))

tree.preOrderTraversal(node)
# root -> left -> right
print()



