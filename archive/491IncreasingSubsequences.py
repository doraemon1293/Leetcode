# coding=utf-8
'''
Created on 2017å¹?6æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = set()
        if n == 0: return[]
        seq = [[[nums[i]]]for i in xrange(n)]
        print seq
        for i in xrange(n - 2, -1, -1):
            for j in xrange(i + 1, n):
                if nums[i] <= nums[j]:
                    for x in seq[j]:
                        seq[i].append([nums[i]] + x)
                        ans.add(tuple([nums[i]] + x))
                    print seq
        return list(ans)


print Solution().findSubsequences([1, 2, 2])

