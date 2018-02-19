# coding=utf-8
'''
Created on 2017å¹?8æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        while n:
            ans.append(n % 9)
            n /= 9
        return int("".join([str(x) for x in ans[::-1]]))
