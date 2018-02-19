# coding=utf-8


class Solution:

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        color = [-1] * len(graph)
        for v in range(len(graph)):
            if color[v] == -1:
                q = deque([v])
                color[v] = 0
                while q:
                    v = q.popleft()
                    for v0 in graph[v]:
                        if color[v0] == -1:
                            color[v0] = (color[v] + 1) % 2
                            q.append(v0)
                        else:
                            if color[v0] == color[v]:
                                return False
        return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(Solution().isBipartite(graph))
