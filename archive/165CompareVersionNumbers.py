# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = map(lambda x: int(x), version1.split("."))
        b = map(lambda x: int(x), version2.split("."))
        for i in range(max((len(a), len(b)))):
            ta = a[i] if i < len(a) else 0
            tb = b[i] if i < len(b) else 0
            if ta > tb:
                return 1
            elif ta < tb:
                return -1
        return 0

