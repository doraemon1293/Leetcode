# coding=utf-8
'''
Created on 2017å¹?6æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0: return 0
        st, en = 0, n - 1
        while st <= en:
            mid = (st + en) / 2
            if n - mid > citations[mid]:
                st = mid + 1
            elif n - mid < citations[mid]:
                en = mid - 1
            else:
                # print "mid", mid
                return citations[mid]
        return n - st


citations = [0, 0, 100]
print Solution().hIndex(citations)
