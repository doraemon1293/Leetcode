# coding=utf-8
'''
Created on 2016å¹?11æœ?15æ—?

@author: Administrator
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 6


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1, n
        while i < j:
            mid = (i + j) / 2
            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1
        return j


print Solution().firstBadVersion(9)
