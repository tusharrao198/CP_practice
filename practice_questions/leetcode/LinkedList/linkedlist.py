class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linkedlist = ""
        while temp:
            linkedlist += str(temp.data) + " "
            temp = temp.next
        return linkedlist

    def insertNode(self, val, pos):
        target = Node(val)
        if pos == 0:
            target.next = self.head
            self.head = target
            return

        count = 1
        prevnode = self.head
        while count < pos:
            prevnode = prevnode.next
            count += 1
        prev_pos = count
        nextnode = prevnode.next
        target.next = nextnode
        prevnode.next = None
        prevnode.next = target

    def deleteNode(self, pos):
        temp = self.head
        if temp is None:
            return
        if pos == 0:
            self.head = temp.next
            temp = None
            return

        prev_pos = 1
        prevnode = self.head
        while prev_pos < pos:
            prevnode = prevnode.next
            prev_pos += 1
        nextnode = prevnode.next.next
        prevnode.next = None
        prevnode.next = nextnode


ll = linkedList()
ll.head = Node(5)

second_node = Node(3)
third_node = Node(1)
fourth_node = Node(6)

ll.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
print(ll.printList())
ll.insertNode(2, 3)
print(ll.printList())

ll.deleteNode(3)
print(ll.printList())
ll.deleteNode(3)
print(ll.printList())
