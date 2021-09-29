# https://www.interviewbit.com/problems/sort-list/

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
		lst = []
		count = 0
		while A:
			lst.append(A.val)
			A = A.next
			count += 1
		lst.sort()
		ans = ListNode(0)
		newhead = ans
		for i in range(count):
			ans.next = ListNode(lst[i])
			ans = ans.next
		return newhead.next
