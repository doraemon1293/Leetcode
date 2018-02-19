# coding=utf-8
'''
Created on 2017å¹?9æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        d = [0] * (n + 1)
        for i in xrange(len(flowers)):
            d[flowers[i]] = i + 1
        ans = float("Inf")
        left = 1
        right = left + k + 1
        while right <= n:
            i = left + 1
            while d[i] > d[left] and d[i] > d[right] and i < right:
                i += 1
            if i == right:
                ans = min(ans, max(d[left], d[right]))
                left += 1
                right = left + k + 1
            else:
                left = i
                right = left + k + 1
        return -1 if ans == float("inf") else ans


flowers = [1, 2, 3]
k = 1
print Solution().kEmptySlots(flowers, k)

