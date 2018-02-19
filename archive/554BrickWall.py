# coding=utf-8
'''
Created on 2017å¹?5æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        c = Counter()
        for row in wall:
            x = 0
            for brick in row[:-1]:
                x += brick
                c.setdefault(x, 0)
                c[x] += 1
        return (len(wall) - c.most_common(1)[0][1]) if c.most_common(1) else len(wall)


# wall = [[1, 2, 2, 1],
#  [3, 1, 2],
#  [1, 3, 2],
#  [2, 4],
#  [3, 1, 2],
#  [1, 3, 1, 1]]
wall = [[1, 1], [2], [1, 1]]
print Solution().leastBricks(wall)

