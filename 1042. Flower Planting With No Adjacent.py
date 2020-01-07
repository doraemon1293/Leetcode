import collections


class Solution:
    def gardenNoAdj(self, N: int, paths):
        adj = collections.defaultdict(set)
        colour = [None] * (N+1)
        for x, y in paths:
            adj[x].add(y)
            adj[y].add(x)
        for i in range(1,N+1):
            # print(set([colour[j] for j in adj[i]]))
            avail = set(range(1, 5)) - set([colour[j] for j in adj[i]])
            print(avail)
            colour[i] = avail.pop()
        return colour[1:]


N = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
print(Solution().gardenNoAdj(N, paths))
