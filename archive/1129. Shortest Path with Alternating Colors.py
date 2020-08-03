import collections


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: list, blue_edges: list) -> list:
        q = collections.deque([(0, "R", 0), (0, "B", 0)])
        edges = collections.defaultdict(set)
        for i, j in red_edges:
            edges[i, "R"].add(j)
        for i, j in blue_edges:
            edges[i, "B"].add(j)
        ans = [float("inf")] * n
        ans[0] = 0

        visited = set([(0, "R"), (0, "B")])
        while q:
            i, c, l = q.popleft()
            next_c="R" if c=="B" else "B"
            for j in edges[i, c]:
                if (j, next_c) not in visited:
                    visited.add((j, next_c))
                    q.append((j, next_c, l + 1))
                    ans[j] = min(ans[j], l + 1)
        ans = [-1 if x == float("inf") else x for x in ans]
        return ans


n = 5
red_edegs = [[0, 1], [1, 2], [2, 3], [3, 4]]
blue_edges = [[1, 2], [2, 3], [3, 1]]
print(Solution().shortestAlternatingPaths(n, red_edegs, blue_edges))
