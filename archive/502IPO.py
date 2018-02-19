# coding=utf-8
'''
Created on 2017å¹?11æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq
        unused = set(range(len(Profits)))
        heap = []

        def pickUp(heap, unused, W):
            temp = set()
            for i in unused:
                if Capital[i] <= W:
                    temp.add(i)
                    heapq.heappush(heap, -Profits[i])
            unused.difference_update(temp)

        for _ in xrange(k):
            pickUp(heap, unused, W)
            if heap:
                W -= heapq.heappop(heap)
            else:
                return W
        return W


k = 1
W = 0
Profits = [1, 2, 3]
Capital = [1, 1, 2]
print Solution().findMaximizedCapital(k, W, Profits, Capital)

