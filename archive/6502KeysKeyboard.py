# coding=utf-8
'''
Created on 2017å¹?7æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        ans = []
        flag = True
        while flag:
            flag = False
            for f in xrange(2, int(n ** 0.5) + 1):
                if n % f == 0:
                    ans.append(f)
                    flag = True
                    n /= f
                    break
        if n != 1: ans.append(n)
        return sum(ans)


n = 100
print Solution().minSteps(n)
