# coding=utf-8
'''
Created on 2017å¹?11æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(asteroids) - 1:
            if asteroids[i] > 0 and asteroids[i + 1] < 0:
                if abs(asteroids[i]) > abs(asteroids[i + 1]):
                    del asteroids[i + 1]
                elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                    del asteroids[i]
                    if i != 0: i -= 1
                else:
                    del asteroids[i]
                    del asteroids[i]
                    if i != 0: i -= 1
            else:
                i += 1
        return asteroids


asteroids = [8, -8]
asteroids = [10, 2, -5]
asteroids = [-2, -2, -2, 1]
print Solution().asteroidCollision(asteroids)
