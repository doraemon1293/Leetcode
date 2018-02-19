# coding=utf-8
'''
Created on 2017å¹?5æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.ans = []

        def dfs(cur, nums, st):
            self.ans.append(cur)
            # print cur
            for i in range(st + 1, len(nums)):
                dfs(cur + [nums[i]], nums, i)

        dfs([], nums, -1)
        self.ans = map(lambda x:list(x), self.ans)
        return self.ans


nums = [1, 2, 2]
print Solution().subsetsWithDup(nums)
