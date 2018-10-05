"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def solve(x1, y1,L):
            temp = [grid[i][j] for i in range(x1, x1+L) for j in range(y1,y1+L)]
            print("temp",temp)
            if all([x == 1 for x in temp]):
                return Node(True, True, None, None, None, None)
            if all([x == 0 for x in temp]):
                return Node(False, True, None, None, None, None)

            return Node(None, False, solve(x1, y1,L//2),
                        solve(x1, y1+L//2,L//2),
                        solve(x1+L//2,y1,L//2),
                        solve(x1+L//2,y1+L/2,L//2))

        return solve(0, 0, len(grid))
