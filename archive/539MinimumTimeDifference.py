# coding=utf-8
'''
Created on 2017å¹?5æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        arr = []
        for timePoint in timePoints:
            arr.append(60 * int(timePoint.split(":")[0]) + int(timePoint.split(":")[1]))
        arr.sort()
        ans = float("inf")
        for i in range(len(arr)):
            diff = abs(arr[i] - arr[(i + 1) % len(arr)])
            if ans > min(diff, 1440 - diff):
                ans = min(diff, 1440 - diff)
        return ans

