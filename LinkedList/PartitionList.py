# https://www.interviewbit.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    
    def SubmittedSolution(self, A, B):
        l1 = ListNode(0)
        l2 = ListNode(0)

        head1, head2 = l1, l2

        while A != None:
            if A.val < B:
                l1.next = A
                l1 = l1.next
                A = A.next

            elif A.val >= B:
                l2.next = A
                l2 = l2.next
                A = A.next

        l1.next = head2.next
        l2.next = None
        return head1.next


    def printList(self, s):
        head = s
        ans = []
        while head!=None:
            ans.append(head.val)
            head=head.next
        print(ans)


    def partition(self, A, B):
        tempend = ListNode(0)  # new list of values >= B
        ehead = tempend # new list head 

        prev = None
        curr = A

        newhead = curr
        while curr != None:
            nextnode = curr.next
            if curr.val >= B:
                if prev == None:  # if current node is first node
                    temp = curr
                    curr = curr.next
                    curr.next = None
                    tempend.next = temp
                    tempend = tempend.next

                else:
                    # print("AA", prev.val, curr.val)
                    prev.next = None
                    prev.next = curr.next
                    curr.next = None
                    tempend.next = curr
                    tempend = tempend.next
            else:
                prev = curr
            curr = nextnode

        prev.next = ehead.next

        self.printList(newhead)
        return newhead.val
        # return newhead

# Approach- greater elements stored in another linked list and deleting from given and then joining its head 

node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(3)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(2)

s = Solution()
x = 3
y = s.partition(node, x)
print(y)
