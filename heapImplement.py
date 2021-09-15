from typing import List
import heapq

arr = [1, 5, 4, 6, 8, 9, 90, 4, 3, 3]

# minheap creation in O(n) time
heapq.heapify(arr)

# heappop method to pop smallest element in O(logn)
x = heapq.heappop(arr)
print(x)

# class  MaxHeap
class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)


# maxheap creation in O(n) time
max_heap = MaxHeap()
for i in arr:
    max_heap.push(i)

# pop, push, top in logn time
y = max_heap.top()
print(y)
