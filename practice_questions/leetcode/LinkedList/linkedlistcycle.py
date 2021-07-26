# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
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
