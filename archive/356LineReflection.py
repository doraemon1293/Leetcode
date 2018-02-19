# coding=utf-8
'''
Created on 2017å¹?6æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        min_x = min([x[0] for x in points])
        max_x = max([x[0] for x in points])
        points = set([tuple(x) for x in points])
        x_line = (float(max_x) + min_x) / 2
        for p in points:
            if (2 * x_line - p[0], p[1]) not in points:
                return False
        return True

