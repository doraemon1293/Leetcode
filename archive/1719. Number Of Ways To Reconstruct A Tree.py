from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = {}
        for a, b in pairs:
            g.setdefault(a, set())
            g.setdefault(b, set())
            g[a].add(b)
            g[b].add(a)
        # print(g)

        def solve(nodes):
            roots = []
            for node in nodes:
                if len(g[node]) == len(nodes) - 1:
                    roots.append(node)
            if len(roots) == 0:
                return 0

            root=roots[0]

            for node in g[root]:
                g[node].remove(root)

            new_nodes = g[root]

            visited = set()
            nodes_sets = []

            def dfs(node):
                for node1 in g[node]:
                    if node1 not in visited:
                        visited.add(node1)
                        nodes_sets[-1].add(node1)
                        dfs(node1)

            for node in new_nodes:
                if node not in visited:
                    nodes_sets.append(set([node]))
                    visited.add(node)
                    dfs(node)
            arr=[solve(nodes) for nodes in nodes_sets]
            if 0 in arr:
                return 0
            if 2 in arr:
                return 2
            if len(roots)>1:
                return 2
            return 1

        return solve(set(g))