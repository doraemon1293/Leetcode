# coding=utf-8
'''
Created on 2016å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n:
            ans += chr((n - 1) % 26 + ord("A"))
            n = (n - 1) / 26
        return ans[::-1]


print Solution().convertToTitle(53)

