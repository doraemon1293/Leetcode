# coding=utf-8
'''
Created on 2017�?5�?14�?

@author: Administrator
'''


# Definition for a point.
class Point(object):

    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b


class Solution(object):

    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if len(points) <= 3: return points
        import math
        import functools

        # 寻找y轴最小的点，如果y轴位置是相同的，那个找x轴位置最小的，称之为基准点�??
        def findMostLeftBottomPoint(points):
            return min(points, key = lambda p: (p.y, p.x))

        def p0IsMostRightPoint(p0, points):
            return p0.x == max([p.x for p in points])

        # 向量p0p1和p0p2的叉�?
        def multiply(p0, p1, p2):
            return (p1.x - p0.x) * (p2.y - p0.y) - (p1.y - p0.y) * (p2.x - p0.x)

        # 求极�?
        def getAngle(p0, p1):
            if p0.x == p1.x:
                if p0.y == p1.y:
                    return 0
                else:
                    return math.pi / 2
            angle = math.atan(float(p1.y - p0.y) / (p1.x - p0.x))
            if angle < 0:
                angle += math.pi
            return angle

        def distance(p0, p1):
            return (p1.y - p0.y) ** 2 + (p1.x - p0.x) ** 2

        def myCmp(p0, p1, p2):
            if getAngle(p0, p1) < getAngle(p0, p2):
                return -1
            elif getAngle(p0, p1) > getAngle(p0, p2):
                return 1
            else:
                # 共线的情�?
                # p2在p0右侧则距离近的排在前
                if p2.x > p0.x:
                    if distance(p0, p1) > distance(p0, p2):
                        return 1
                    else:
                        return -1
                # p2在p0左侧则按距离远的排在�?
                elif p2.x < p0.x:
                    if distance(p0, p1) > distance(p0, p2):
                        return -1
                    else:
                        return 1
                # p0,p1,p2垂直于x�?
                else:
                    # 如果p0是points里最右的�? 则距离近的排在前
                    if p0IsMostRightPoint:
                        if distance(p0, p1) > distance(p0, p2):
                            return 1
                        else:
                            return -1
                    else:
                        if distance(p0, p1) > distance(p0, p2):
                            return -1
                        else:
                            return 1

        # 按照极角排序
        def sortByAngle(p0, points):
            return sorted([point for point in points if point != p0], cmp = functools.partial(myCmp, p0))

        p0 = findMostLeftBottomPoint(points)
        p0IsMostRightPoint = p0IsMostRightPoint(p0, points)
        points = sortByAngle(p0, points)
        print p0.x, p0.y
        print [(p.x, p.y) for p in points]
        stack = [p0, points[0]]
        for i in range(1, len(points)):
            while len(stack) >= 2 and multiply(stack[-2], stack[-1], points[i]) < 0:
                stack.pop()
            stack.append(points[i])
        return stack


arr = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
arr = [[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [4, 5], [3, 5], [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]]
arr = [[0, 2], [0, 4], [0, 5], [0, 9], [2, 1], [2, 2], [2, 3], [2, 5], [3, 1], [3, 2], [3, 6], [3, 9], [4, 2], [4, 5], [5, 8], [5, 9], [6, 3], [7, 9], [8, 1], [8, 2], [8, 5], [8, 7], [9, 0], [9, 1], [9, 6]]
points = [Point(x, y) for x, y in arr]
print [(p.x, p.y) for p in Solution().outerTrees(points)]

