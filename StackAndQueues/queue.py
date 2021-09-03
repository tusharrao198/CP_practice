from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def top(self):
        return self.q[0]

    def pop(self):
        return self.q.popleft()

    def enqueue(self, val):
        self.q.append(val)

    def isEmpty(self):
        return True if len(self.q == 0) else False


q = Queue()
q.enqueue(5)
q.enqueue(2)
q.enqueue(3)
q.enqueue(6)
q.enqueue(8)
q.enqueue(1)

print(q.top())
print(q.pop())
print(q.top())
