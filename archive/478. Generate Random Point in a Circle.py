import random
import math


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center, self.y_center = x_center, y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        radius = random.random()**0.5*self.radius
        angle = random.random()*2 * math.pi
        return [self.x_center + math.cos(angle) * radius, self.y_center + math.sin(angle) * radius]


# Your Solution object will be instantiated and called as such:
# radius, x_center, y_center = [0.01, -73839.1, -3289891.3]
# obj = Solution(radius, x_center, y_center)
# print(obj.randPoint())
