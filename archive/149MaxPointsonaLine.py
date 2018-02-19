# coding=utf-8
'''
Created on 2017å¹?7æœ?4æ—?

@author: Administrator
'''


# Definition for a point.
class Point(object):

    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        def gcd(a, b):
            siga = -1 if a < 0 else 1
            sigb = -1 if b < 0 else 1
            a = abs(a)
            b = abs(b)
            if a == 0 and b == 0:return(0, 0)
            if b == 0:return (1, 0)
            if a == 0:return (0, 1)
            if a < b:
                swapped = True
                a, b = b, a
            else:
                swapped = False
            ta, tb = a, b
            while ta % tb != 0:
                ta, tb = tb, ta % tb
            if swapped:
                return (siga * sigb * (b / tb), a / tb)
            else:
                return (siga * sigb * (a / tb), b / tb)

        from collections import defaultdict
        maxi = 1 if points else 0
        for i in xrange(len(points)):
            d = defaultdict(int)
            overlap = 1
            for j in xrange(i + 1, len(points)):
                if (points[i].x, points[i].y) == (points[j].x, points[j].y):
                    overlap += 1
                else:
                    d[gcd(points[j].y - points[i].y, points[j].x - points[i].x)] += 1
            maxi = max(maxi, overlap)
            for v in d.values():
                maxi = max(maxi, v + overlap)
        return maxi


arr = [[-435, -347], [-435, -347], [609, 613], [-348, -267], [-174, -107], [87, 133], [-87, -27], [-609, -507], [435, 453], [-870, -747], [-783, -667], [0, 53], [-174, -107], [783, 773], [-261, -187], [-609, -507], [-261, -187], [-87, -27], [87, 133], [783, 773], [-783, -667], [-609, -507], [-435, -347], [783, 773], [-870, -747], [87, 133], [87, 133], [870, 853], [696, 693], [0, 53], [174, 213], [-783, -667], [-609, -507], [261, 293], [435, 453], [261, 293], [435, 453]]
points = [Point(a, b) for a, b in arr]

print Solution().maxPoints(points)

