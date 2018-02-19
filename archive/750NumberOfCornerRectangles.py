# coding=utf-8
'''
Created on 18 Dec 2017

@author: Administrator
'''


class Solution(object):

    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)
        ans = 0
        for row in grid:
            row = [i for i, x in enumerate(row) if x]
            for i in range(len(row)):
                for j in range(i + 1, len(row)):
                    count[row[i], row[j]] += 1
        ans = sum([x * (x - 1) // 2 for x in count.values()])
        return ans


grid = [[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
print(Solution().countCornerRectangles(grid))

