# coding=utf-8
'''
Created on 2016å¹?11æœ?9æ—?

@author: Administrator
'''


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in xrange(numRows):
            if row == 0:
                current_row = [1]
            else:
                current_row = []
                for j in xrange(row + 1):
                    current_row.append((ans[-1][j - 1] if j != 0 else 0) + (ans[-1][j] if j != row else 0))
            ans.append(current_row)
        return ans


print Solution().generate(10)
