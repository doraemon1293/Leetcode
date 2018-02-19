# coding=utf-8
'''
Created on 2017å¹?10æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict, Counter
        inds = {}
        count = Counter(nums)
        for i, num in enumerate(nums):
            inds.setdefault(num, [float("inf"), -float("inf")])
            inds[num][0] = min(inds[num][0], i)
            inds[num][1] = max(inds[num][1], i)
            count[num] += 1
        ans = float("inf")
        maxi = None
        for num, freq in count.most_common():
            if maxi == None:
                maxi = freq
            if freq < maxi:
                break
            ans = min(ans, inds[num][1] - inds[num][0] + 1)
        return ans


nums = [3, 1, 2, 2, 2, 1, 4, 3, 3, 3]
nums = [1]
print Solution().findShortestSubArray(nums)
