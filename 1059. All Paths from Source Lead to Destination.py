class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for a, b in edges:
            graph.setdefault(a, [])
            graph[a].append(b)
        if destination in graph:
            return False

        def dfs(a,visited):
            print(a)
            if a in visited:
                return False
            if a == destination:
                return True
            visited.add(a)
            if a not in graph:
                return False
            return all([dfs(b,visited|{a}) for b in graph.get(a, [])])
        return dfs(source,set())
