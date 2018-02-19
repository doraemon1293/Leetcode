# coding=utf-8
'''
Created on 2017å¹?11æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        stack = [(sr, sc)]
        colour = image[sr][sc]
        m, n = len(image), len(image[0])
        visited = set()
        while stack:
            x, y = stack.pop()
            image[x][y] = newColor
            visited.add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < m and 0 <= y1 < n and image[x1][y1] == colour and (x1, y1) not in visited:
                    stack.append((x1, y1))
        return image


image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
newColor = 1
print Solution().floodFill(image, sr, sc, newColor)
