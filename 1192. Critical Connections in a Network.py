# Python program to find bridges in a given undirected graph
# Complexity : O(V+E)

from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections: list) -> list:
        self.g = defaultdict(list)
        for u, v in connections:
            self.g[u].append(v)
            self.g[v].append(u)

        '''A recursive function that finds and prints bridges 
        using DFS traversal 
        u --> The vertex to be visited next 
        visited[] --> keeps tract of visited vertices 
        disc[] --> Stores discovery times of visited vertices 
        parent[] --> Stores parent vertices in DFS tree'''

        self.visited = set()
        self.disc = [float("inf")] * n
        self.low = [float("inf")] * n
        self.disc_time = 0
        self.parent = {}
        self.ans = []

        def dfs(u):
            self.visited.add(u)
            self.disc[u] = self.disc_time
            self.low[u] = self.disc_time
            self.disc_time += 1
            for v in self.g[u]:
                if v not in self.visited:
                    self.parent[v] = u
                    dfs(v)
                    self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] > self.disc[u]:
                    self.ans.append((u, v))
                elif v != self.parent.get(u, None):
                    self.low[u] = min(self.low[u], self.disc[v])

        dfs(0)
        return self.ans


n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(Solution().criticalConnections(n, connections))
