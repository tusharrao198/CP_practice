# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        turtle = A
        hare = A

        isCycle = False
        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                isCycle = True
                break

        if not isCycle:
            return None

        # if crossed this condtion then it's sure that there is a cycle present
        # so we check the node where the cycle begins
        # keeping turtle at head and incrementing to know the cycle
        turtle = A
        while turtle != hare:
            turtle = turtle.next
            hare = hare.next
        return turtle

    def hasCycle(self, head: ListNode) -> bool:
        # using two pointers turtle and hare set to head
        turtle = head
        hare = head

        # hare.next condition because hare is incremented by twice,
        # so need to check if next exists then only nect.next exists
        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                return True
        return False


s = Solution()

node1 = ListNode(1)
node2 = ListNode(5)
node3 = ListNode(11)
node4 = ListNode(8)
node5 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node2

ans = s.hasCycle(node1)
print(ans)
