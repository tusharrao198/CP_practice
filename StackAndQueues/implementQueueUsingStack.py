class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self) -> str:
        ans = [str(i) for i in self.s1][::-1]
        return " ".join(ans)

    def enqueue(self, val):

        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(val)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            return None
        return self.s1.pop()


S = Queue()
S.enqueue(2)
S.enqueue(3)
S.enqueue(5)
S.enqueue(1)
S.enqueue(7)
S.enqueue(9)
print(S)

print(S.dequeue())
print(S)
