# coding=utf-8
'''
Created on 2016å¹?12æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.insert(0, -float("inf"))
        heaters.append(float("inf"))
        heaters.sort()
        i = 0
        ans = -float("inf")
        for house in houses:
            while not (heaters[i] <= house <= heaters[i + 1]):
                i += 1
            ans = max(ans, min(abs(heaters[i] - house), abs(heaters[i + 1] - house)))
        return ans


houses = [1, 2, 3]
heaters = [2]
print Solution().findRadius(houses, heaters)
