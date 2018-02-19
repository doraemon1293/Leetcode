# coding=utf-8
'''
Created on 2017å¹?4æœ?18æ—?

@author: Administrator
'''


class Solution(object):

    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = [str(i) for i in range(1, n + 1)]
        while len(ans) > 1:
            temp = []
            for x in range(len(ans) / 2):
                temp.append("(" + ans[x] + "," + ans[-x - 1] + ")")
            ans = temp
        return ans[0]


print Solution().findContestMatch(32)
