# coding=utf-8
'''
Created on 2017å¹?5æœ?26æ—?

@author: Administrator
'''
from copy import copy


class Solution(object):

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ans = ""
        d1 = copy(d)
        for ch in s:
            for i in range(len(d1)):
                if d1[i] and d1[i][0] == ch:
                    d1[i] = d1[i][1:]
        for i in range(len(d1)):
            if d1[i] == "":
                if len(d[i]) > len(ans) or len(d[i]) == len(ans) and ans > d[i]:
                    ans = d[i]
        return ans


s = "apple"
d = ["zxc", "vbn"]
print Solution().findLongestWord(s, d)
