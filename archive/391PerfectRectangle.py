# coding=utf-8
'''
Created on 2017å¹?9æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        sumOfarea = 0
        min_x = float("inf")
        min_y = float("inf")
        max_x = -float("inf")
        max_y = -float("inf")
        pointsSet = set()
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            for x, y in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if (x, y) in pointsSet:
                    pointsSet.remove((x, y))
                else:
                    pointsSet.add((x, y))
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            sumOfarea += (x2 - x1) * (y2 - y1)
        # 1 4
        # 2 3
        cornerPoints = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        print cornerPoints, pointsSet
        print sumOfarea, (max_x - min_x) * (max_y - min_y)
        if (max_x - min_x) * (max_y - min_y) == sumOfarea and cornerPoints == pointsSet:
            return True
        else:
            return False


rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]

print Solution().isRectangleCover(rectangles)

