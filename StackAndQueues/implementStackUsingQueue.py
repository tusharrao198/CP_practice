from collections import deque

# implementing stack using queue


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()  # acting as a backup

    def __str__(self) -> str:
        ans = [str(self.q1[i]) for i in reversed(range(len(self.q1)))]
        return " ".join(ans)

    def push(self, val):
        while len(self.q1) > 0:
            x = self.q1.popleft()
            self.q2.append(x)

        self.q1.append(val)

        while len(self.q2) > 0:
            x = self.q2.popleft()
            self.q1.append(x)

    def top(self):
        return self.q1[0]

    def pop(self):
        return self.q1.popleft() if len(self.q1) > 0 else "IS EMPTY"


s = Stack()
arr = [3, 1, 2, 5, 4, -1, -8]
s.push(3)
s.push(1)
s.push(2)
s.push(5)
s.push(4)
print(s.top())
print(s)
print(s.pop())
print(s)
