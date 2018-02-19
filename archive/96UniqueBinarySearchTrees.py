# coding=utf-8
'''
Created on 2017å¹?5æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1]
        for nn in range(1, n + 1):
            total = 0
            for i in range(1, nn + 1):
                total += ans[i - 1] * ans[nn - i]
            ans.append(total)
        return ans[n]


print Solution().numTrees(3)
