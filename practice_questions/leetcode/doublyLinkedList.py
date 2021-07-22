class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer
        self.prev = None  # pointer


class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self, arr):
        start = self.head
        temp = start
        for i in range(len(arr)):
            newnode = Node(arr[i])
            if i == 0:
                start = newnode
                temp = start
            else:
                temp.next = newnode
                newnode.prev = temp
                temp = temp.next
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linkedlist = ""
        while temp:
            linkedlist += str(temp.data) + " "
            temp = temp.next
        return linkedlist

    def countList(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    # here in insert index >=1
    def insert(self, val, index):
        temp = self.head
        count = self.countList()

        if count + 1 < index:
            print(
                f"# for case when we want to insert element at index 6 in array of length of 4 even though no node at 5"
            )
            return temp

        newnode = Node(val)
        if index == 1:  # inital
            newnode.next = temp
            temp.prev = newnode
            self.head = newnode
            return self.head

        if index == count + 1:  # last
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
            return self.head

        i = 1
        while i < index:
            temp = temp.next
            i += 1
        prev_pos = i
        prev_node = temp

        nodeAtTarget = prev_node.next

        newnode.next = nodeAtTarget
        nodeAtTarget.prev = newnode

        prev_node.next = newnode
        newnode.prev = prev_node

        return self.head

    def delete(self, index):
        temp = self.head
        count = self.countList()
        if count < index:
            print(f"# can't delete node greater than length")
            return temp

        if index == 1:
            newhead = temp.next
            newhead.prev = None
            self.head = newhead
            return self.head

        if index == count:  # for last
            # get prev node of the last
            while temp.next is not None and temp.next.next is not None:
                temp = temp.next
            temp.next = None
            return self.head

        i = 1
        while i < index:
            temp = temp.next
            i += 1
        prev_pos = i
        prev_node = temp

        next_val = prev_node.next.next  # next to next value of prev node

        prev_node.next = next_val
        next_val.prev = prev_node

        return self.head


arr = [1, 2, 3, 4, 5, 6]
ll = LinkedList()
ll.createLinkedList(arr)
print(ll.printList())
ll.insert(2, 3)
print(ll.printList())
ll.delete(3)
print(ll.printList())
