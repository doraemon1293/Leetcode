from collections import deque


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)

        def find_ones(A):
            return [(i, j) for i in range(N) for j in range(N) if A[i][j]]

        def find_islands(A):
            ones = find_ones(A)
            i, j = ones[0]
            ones = set(ones)
            ones.remove((i, j))
            q = deque([(i, j)])
            island1 = set([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x1, y1 = x + dx, y + dy
                    if (x1, y1) in ones:
                        ones.remove((x1,y1))
                        q.append((x1, y1))
                        island1.add((x1, y1))
            island2 = ones
            return island1, island2

        def find_shortest_distance(island1, island2):
            q = deque([(i, j, 0) for i, j in island1])
            visited = set()
            while q:
                x, y, steps = q.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x1, y1 = x + dx, y + dy
                    if (x1,y1) in island2:
                        return steps
                    if 0 <= x1 < N and 0 <= y1 < N and A[x1][y1] == 0 and (x1, y1) not in visited:
                        visited.add((x1, y1))
                        q.append((x1, y1, steps + 1))


        island1, island2 = find_islands(A)
        return find_shortest_distance(island1, island2)


A =[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
A= [[0,1,0],[0,0,0],[0,0,1]]
print(Solution().shortestBridge(A))
