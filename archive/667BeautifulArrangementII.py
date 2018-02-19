# coding=utf-8
'''
Created on 2017å¹?8æœ?29æ—?

@author: Administrator
'''


class Solution(object):

    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = [1]
        inc = True
        l, r = 1, n + 1
        for _ in xrange(k - 1):
            if inc:
                r -= 1
                ans.append(r)
            else:
                l += 1
                ans.append(l)
            inc = not inc
        if inc:
            ans.extend(range(l + 1, r))
        else:
            ans.extend(range(r - 1, l, -1))
        return ans


print Solution().constructArray(10, 5)
