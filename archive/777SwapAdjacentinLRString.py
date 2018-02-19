# coding=utf-8
'''
Created on 12 Feb 2018

@author: Administrator
'''


class Solution(object):

    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end) or start.replace("X", "") != end.replace("X", ""):
            return False
        rSarr = [i for i in range(len(start)) if start[i] == "R"]
        lSarr = [i for i in range(len(start)) if start[i] == "L"]
        rEarr = [i for i in range(len(start)) if end[i] == "R"]
        lEarr = [i for i in range(len(start)) if end[i] == "L"]
        if len(rSarr) != len(rEarr) or len(lSarr) != len(lEarr):
            return False
        for i in range(len(rSarr)):
            if rSarr[i] > rEarr[i]:
                return False
        for i in range(len(lSarr)):
            if lSarr[i] < lEarr[i]:
                return False
        return True


start = "RL"
end = "LR"
print(Solution().canTransform(start, end))
