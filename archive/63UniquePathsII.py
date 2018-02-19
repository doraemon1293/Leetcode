# coding=utf-8
'''
Created on 2016å¹?12æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [0] * n
        for i in xrange(m):
            last_ans = ans
            ans = []
            for j in xrange(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        ans.append(1)
                    else:
                        ans.append((ans[-1] if j != 0 else 0) + last_ans[j])
                else:
                    ans.append(0)
        print ans
        return ans[-1]

