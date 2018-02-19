# coding=utf-8
'''
Created on 2017å¹?8æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # cross product of vector AB AC >0 =>0 A->B->C is counterclockwise
        # cross product of vector AB AC <0 =>0 A->B->C is clockwise
        n = len(points)

        def cross(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        last = 0
        for i in xrange(n):
            a, b, c = points[i], points[(i + 1) % n], points[(i + 2) % n]
            p = cross(a, b, c)
            if p == 0:
                continue
            if last * cross(a, b, c) < 0:
                return False
            last = p
        return True
