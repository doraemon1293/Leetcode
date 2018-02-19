# coding=utf-8
'''
Created on 2016å¹?11æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        inc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = [[None] * n for i in xrange(n)]
        d = x = y = 0
        for i in xrange(1, n ** 2 + 1):
            ans[x][y] = i
            t_x, t_y = x + inc[d][0], y + inc[d][1]
            if t_x < 0 or t_x >= n or t_y < 0 or t_y >= n or ans[t_x][t_y] != None:
                d = (d + 1) % 4
            t_x, t_y = x + inc[d][0], y + inc[d][1]
            x, y = t_x, t_y
        return ans


for x in Solution().generateMatrix(5):
    print x

