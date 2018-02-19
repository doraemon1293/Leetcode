# coding=utf-8
'''
Created on 2017å¹?9æœ?25æ—?

@author: Administrator
'''


class Solution(object):

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if heightMap == []: return 0
        import heapq
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in xrange(m)]
        heap = []
        for i in xrange(m):
            if visited[i][0] == False:
                heapq.heappush(heap, (heightMap[i][0], i, 0))
                visited[i][0] = True
            if visited[i][n - 1] == False:
                heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
                visited[i][n - 1] = True
        for j in xrange(n):
            if visited[0][j] == False:
                heapq.heappush(heap, (heightMap[0][j], 0, j))
                visited[0][j] = True
            if visited[m - 1][j] == False:
                heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
                visited[m - 1][j] = True
        ans = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and visited[x][y] == False:
                    ans += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = True
        return ans


heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
# heightMap = [[12, 13, 1, 12],
#              [13, 4, 13, 12],
#              [13, 8, 10, 12],
#              [12, 13, 12, 12],
#              [13, 13, 13, 13]]
print Solution().trapRainWater(heightMap)
