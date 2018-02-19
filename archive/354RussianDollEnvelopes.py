# coding=utf-8
'''
Created on 2017å¹?11æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect
        nums = [x[1] for x in sorted(envelopes, cmp = lambda x, y:x[0] - y[0] if x[0] != y[0] else y[1] - x[1])]
        arr = []
        for num in nums:
            ind = bisect.bisect_left(arr, num)
            if ind == len(arr):
                arr.append(num)
            else:
                arr[ind] = min(arr[ind], num)
        return len(arr)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print Solution().maxEnvelopes(envelopes)
