class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import itertools
        points = set(tuple(x) for x in points)
        ans = float("inf")
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = (p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1])
            if p4 in points and p4 not in (p1,p2,p3):
                # (p2-p1).(p3-p2)
                if abs((p1[0] - p2[0]) * (p3[0] - p2[0]) + (p1[1] - p2[1]) * (p3[1] - p2[1])) < 10 ** (-7):
                    area = (((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5) * (
                            ((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2) ** 0.5)
                    ans = min(ans, area)
        return ans if ans != float("inf") else 0


points = [[1, 2], [2, 1], [1, 0], [0, 1]]
points = [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]
print(Solution().minAreaFreeRect(points))
