
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1,v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def printGraph(self):
        for node in self.graph:
             for v in self.graph[node]:
                 print(node, " => ", v)
        # OR 
        # for node, v in self.graph.items():
        #     #  for v in self.graph[node]:
        #     print(node, " => ", v)

    
g = Graph()
g.insertEdge(1,5)
g.insertEdge(1,12)
g.insertEdge(5,2)
g.insertEdge(2,7)
g.insertEdge(7,1)

print(g.printGraph())

# -------------------------------
# with inputs
tt = int(input())
for _ in range(tt):
    nodes = int(input())
    lst = list(map(int, input().split()))
    g = Graph()
    for edge in range(nodes-1):
        u, v = map(int, input().split())
        g.insertEdge(u, v)
    g.printGraph()

