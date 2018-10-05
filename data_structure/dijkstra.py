from collections import defaultdict
from heapq import *


def dijkstra(edges, source, target):
    g = defaultdict(list)
    d = defaultdict(lambda: (float("inf"), None))
    d[source] = (0, None)
    for u, v, dis in edges:
        g[u].append((v, dis))
    q = [(0, source)]
    visited = set()
    while q:
        dis, u = heappop(q)
        if u not in visited:
            visited.add(u)
            if u == target:
                return dis
            for v, dis in g.get(u, ()):
                if d[v][0] > d[u][0] + dis:
                    d[v] = (d[u][0] + dis, u)
                    heappush(q, (d[v][0], v))
    return d[target][0]


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

print("=== Dijkstra ===")
# print(edges)
print("A -> E:")
print(dijkstra(edges, "A", "E"))
print("F -> G:")
print(dijkstra(edges, "F", "G"))
