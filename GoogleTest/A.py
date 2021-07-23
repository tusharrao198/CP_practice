
#######################################

# INCOMPLETE

############################
from collections import defaultdict


# Binary Tree Node
class newNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def printGraph(self):
        lst = []
        for node in self.graph:
            for v in self.graph[node]:
                lst.append([node, v])
                # print(node, " => ", v)
        return lst


    def printNodesAtLevelOfTree(self, root):
        if not root: return
        q = [root]
        count = 1
        level_nodes = [[1, q[0].val]]
        while len(q):
            count += 1
            n = len(q)  # number of nodes at current level
            # Traverse all nodes of current level
            for i in range(1, n + 1):
                temp = q[0]
                print("F ", temp.left)
                q.pop(0)
                if temp.left is not None: q.append(temp.left)
                if temp.right is not None: q.append(temp.right)
            if len(q) != 0:
                print(count, q)
                level_nodes.append([count, [i.val for i in q]])
        return level_nodes


tt = int(input())
for _ in range(tt):
    nodes = int(input())
    nums = list(map(int, input().split()))
    g = Graph()
    for edge in range(nodes - 1):
        u, v = map(int, input().split())
        g.insertEdge(newNode(nums[u - 1]), newNode(nums[v - 1]))

    lst = g.printGraph()
    odd = []
    even = []

    print(g.printNodesAtLevelOfTree(lst[0][0]))

    # g.printGraph()
