# coding=utf-8
'''
Created on 2017å¹?9æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def dfs(point):
            if point in memo:
                return memo[point]
            else:
                x, y = point
                res = max([dfs((x + dx, y + dy)) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)) if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x + dx][y + dy] > matrix[x][y]] + [0]) + 1
                memo[point] = res
                return res

        if matrix == []: return 0
        m, n = len(matrix), len(matrix[0])
        memo = {}
        ans = 0
        for x in xrange(m):
            for y in xrange(n):
                ans = max(ans, dfs((x, y)))
        return ans


matrix = [
  [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1]
]
print Solution().longestIncreasingPath(matrix)
