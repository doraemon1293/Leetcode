# coding=utf-8
'''
Created on 2016�?10�?27�?

@author: Administrator
'''


class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for c in s:
            ans = ans * 26 + ord(c) - ord("A") + 1
        return ans


print Solution().titleToNumber("AA")
