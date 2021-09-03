# https://leetcode.com/problems/course-schedule-ii/submissions/

class Solution:

    def detectCycleMain(self, adj, visited, v):

        if visited[v] == 1:
            return True

        if visited[v] == 2:
            return False

        visited[v] = 1

        for i in range(len(adj[v])):

            if self.detectCycleMain(adj, visited, adj[v][i]):
                return True

        visited[v] = 2
        return False

    def detectCycle(self, adj, n):

        visited = [0] * n

        for i in range(n):
            if visited[i] == 0:
                if self.detectCycleMain(adj, visited, i):
                    return True
        return False

    def dfs(self, adj, visited, v, stack):
        visited[v] = True
        for i in range(len(adj[v])):
            if not visited[adj[v][i]]:
                self.dfs(adj, visited, adj[v][i], stack)
        stack.append(v)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        ans = []

        if self.detectCycle(adj, numCourses):
            return ans

        # if cycle not detected then apply topological sort using dfs + stack
        stack = []
        visited = [False] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                self.dfs(adj, visited, i, stack)

        while len(stack) > 0:
            ans.append(stack.pop())

        return ans
