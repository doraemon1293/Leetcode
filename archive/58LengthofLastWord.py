# coding=utf-8
'''
Created on 2016�?11�?14�?

@author: Administrator
'''


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(" ")[-1])


print Solution().lengthOfLastWord("a")
