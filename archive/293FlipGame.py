# coding=utf-8
'''
Created on 2016�?12�?1�?

@author: Administrator
'''


class Solution(object):

    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in xrange(len(s) - 1):
            if s[i] == s[i + 1] == "+":
                ans.append(s[:i] + "--" + s[i + 2:])
        return ans
