# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> int:
#
#
#    def isTarget(self) -> None:
#
#
import heapq


class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        grid = {(0, 0): 0}
        self.target = None

        def dfs(x, y):
            for d, rd, dx, dy in (('U', 'D', 1, 0), ('D', 'U', -1, 0), ('L', 'R', 0, -1), ('R', 'L', 0, 1)):
                x1, y1 = x + dx, y + dy
                if (x1, y1) not in grid:
                    if master.canMove(d):
                        grid[(x1, y1)] = master.move(d)
                        if master.isTarget():
                            self.target = (x1, y1)
                        dfs(x1, y1)
                        master.move(rd)

        dfs(0, 0)

        least_cost = {}

        def shortest_path(target):
            heap = [(0, 0, 0)]
            while heap:
                cost, x, y = heapq.heappop(heap)
                least_cost[x, y] = cost
                if (x, y) == target:
                    return cost
                for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                    x1, y1 = x + dx, y + dy
                    if (x1, y1) in grid and (x1, y1) not in least_cost:
                        heapq.heappush(heap, (cost + grid[x1, y1], x1, y1))

        if self.target == None:
            return -1
        else:
            return shortest_path(self.target)