# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        current_row = last_row = [1]
        for row in xrange(1, rowIndex + 1):
            current_row = []
            for j in xrange(row + 1):
                current_row.append((last_row[j - 1] if j != 0 else 0) + (last_row[j] if j != row else 0))
            last_row = current_row
        return current_row


print Solution().getRow(2)
