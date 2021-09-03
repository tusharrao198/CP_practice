# https://leetcode.com/problems/course-schedule/submissions/

from typing import List

# TC:- O(V+E)
# Sace Complexity:- O(V+E)

class Solution:
    def detectCycle(self, adj, visited, cur):
        if visited[cur] == 2:
            return True

        visited[cur] = 2
        # print("A ", len(adj[cur]))
        for i in range(len(adj[cur])):
            # print(adj[cur][i], adj[cur])
            if visited[adj[cur][i]] != 1:  # skipping nodes that are under processing

                if self.detectCycle(adj, visited, adj[cur][i]):

                    return True

        visited[cur] = 1

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])

        # 2-> processing
        # 1 -> processed
        # 0 -> unprocessed

        visited = [0] * numCourses

        for i in range(numCourses):
            if visited[i] == 0: # check for unprocessed node
                if self.detectCycle(adj, visited, i): # check for cycle 
                    return False
        return True

s = Solution()
prerequisites = [[1,0]]
n = 2
ans = s.canFinish(n, prerequisites)
print(ans)
