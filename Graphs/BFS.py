from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def BFS(self, startNode):
        visited = set()
        queue = []  # queue
        queue.append(startNode)
        visited.add(startNode)

        while (len(queue)):
            cur = queue.pop(0) # popped first element and stored in cur
            print(cur, end=" ")

            for node in self.graph[cur]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)

g = Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.BFS(2)  # it will traverse the tree level by level

