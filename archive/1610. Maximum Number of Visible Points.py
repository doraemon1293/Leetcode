import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        points_angle = []
        same_points = 0
        x0, y0 = location
        for x1, y1 in points:
            if x1 == x0 and y1 == y0:
                same_points += 1
            else:
                points_angle.append(math.atan2(y1 - y0, x1 - x0))

        points_angle.sort()
        points_angle = points_angle + [x + 2 * math.pi for x in points_angle]
        angle = angle * math.pi / 180
        p1 = p2 = 0
        ans = 0
        for p2 in range(len(points_angle)):
            while points_angle[p2] - points_angle[p1] > angle:
                p1 += 1
            ans = max(ans, p2 - p1 + 1)
        return ans + same_points


