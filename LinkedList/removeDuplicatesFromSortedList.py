# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
		if A is None: return A
		prev = A
		head = A
		A = A.next
		while A and A.next:
			if A.val== prev.val:
				prev.next = A.next
				A = A.next
			else:
				prev = A
				A = A.next
		
		if A is not None and A.val==prev.val:
			prev.next = None
		return head
