# coding=utf-8
'''
Created on 2017å¹?5æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        x_min, x_max = float("inf"), -float("inf")
        y_min, y_max = float("inf"), -float("inf")
        for i in xrange(len(image)):
            for j in xrange(len(image[0])):
                if image[i][j] == "1":
                    x_min = min(x_min, i)
                    x_max = max(x_max, i)
                    y_min = min(y_min, j)
                    y_max = max(y_max, j)
        # print x_min, y_min, x_max, y_max
        return  (x_max - x_min + 1) * (y_max - y_min + 1)


image = [
  "0010",
  "0110",
  "0100"
]
x = 0
y = 2

print Solution().minArea(image, x, y)
