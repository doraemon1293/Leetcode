import collections
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        Because xi < xj,
        yi + yj + |xi - xj| = (yi - xi) + (yj + xj)
        So we only need to find out the maximum yi - xi.
        """
        q = collections.deque()  # q[0][0]=y-x q[0][1]=x
        ans = -float("inf")
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                ans = max(ans, q[0][0] + x + y)
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append((y - x, x))
            # print(q)
        return ans


points = [[1, 3], [2, 0], [5, 10], [6, -10]]
k = 1
points = [[0, 0], [3, 0], [9, 2]]
k = 3
points = [[-17, 13], [2, 1], [8, -5], [18, -20]]
k = 26
points = [[-19, -12], [-13, -18], [-12, 18], [-11, -8], [-8, 2], [-7, 12], [-5, 16], [-3, 9], [1, -7], [5, -4],
          [6, -20], [10, 4], [16, 4], [19, -9], [20, 19]]
k = 6
print(Solution().findMaxValueOfEquation(points, k))
