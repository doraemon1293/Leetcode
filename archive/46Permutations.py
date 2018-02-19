# coding=utf-8
'''
Created on 2016å¹?11æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for arr in ans:
                for i in xrange(len(arr) + 1):
                    new_ans.append(arr[:i] + [n] + arr[i:])
            ans = new_ans
        return ans


nums = [-1, -2, -3, -4]
nums = [8, 2, -1, 6]
print Solution().permute(nums)
print len(Solution().permute(nums))

