# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        ans = 0
        add = False
        for x in Counter(s).values():
            if x % 2:
                add = True
                ans += x - 1
            else:
                ans += x
        if add:
            ans += 1
        return ans

