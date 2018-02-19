# coding=utf-8
'''
Created on 2017å¹?7æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        if matrix == []: return []
        m, n = len(matrix), len(matrix[0])
        # pacific
        q = deque([(0, x) for x in xrange(n)] + [(x, 0) for x in xrange(m)])
        visited = set(q)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                if 0 <= dx + x < m and 0 <= dy + y < n and (dx + x, dy + y) not in visited and matrix[dx + x][dy + y] >= matrix[x][y]:
                    q.append((dx + x, dy + y))
                    visited.add((dx + x, dy + y))
        pacific = visited
        # atlantic
        q = deque([(m - 1, x) for x in xrange(n)] + [(x, n - 1) for x in xrange(m)])
        visited = set(q)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                if 0 <= dx + x < m and 0 <= dy + y < n and (dx + x, dy + y) not in visited and matrix[dx + x][dy + y] >= matrix[x][y]:
                    q.append((dx + x, dy + y))
                    visited.add((dx + x, dy + y))
        atlantic = visited
        return list(pacific & atlantic)
        # return sorted(list(pacific & atlantic))


matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print Solution().pacificAtlantic(matrix)

