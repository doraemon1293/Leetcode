# coding=utf-8
'''
Created on 2016å¹?11æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points == []:return 0
        points.sort()
        arrow_point = points[0]
        ans = 1
        for point in points:
            if arrow_point[0] <= point[0] <= arrow_point[1]:
                arrow_point = ((max(arrow_point[0], point[0])), min(arrow_point[1], point[1]))
            else:
                ans += 1
                arrow_point = point
        return ans

