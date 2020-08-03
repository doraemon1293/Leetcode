from collections import defaultdict


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_points = defaultdict(set)
        for x, y in points:
            x_points[x].add(y)
        ans = float("inf")
        for x1 in x_points:
            for x2 in x_points:
                if x1 != x2:
                    y_points = x_points[x1] & x_points[x2]
                    if len(y_points)>1:
                        min_y_distance = min([abs(y1 - y2) for y1 in y_points for y2 in y_points if y1 != y2])
                        ans = min(ans, abs(x2 - x1) * min_y_distance)
        return 0 if ans==float("inf") else ans
