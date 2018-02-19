# coding=utf-8
'''
Created on 2017å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dp = [defaultdict(int) for _ in xrange(len(A))]
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(i):
                dp[i][A[i] - A[j]] += 1
                if A[i] - A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i] - A[j]]
                    ans += dp[j][A[i] - A[j]]
        return ans


A = [2, 4, 6, 8, 10]
print Solution().numberOfArithmeticSlices(A)
