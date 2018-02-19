# coding=utf-8
'''
Created on 2017å¹?8æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # return list(set(itertools.permutations(nums)))

        ans = [[]]
        for n in nums:
            new_ans = []
            for arr in ans:
                for i in xrange(len(arr) + 1):
                    new_ans.append(arr[:i] + [n] + arr[i:])
                    if i < len(arr) and arr[i] == n: break
            print new_ans
            ans = new_ans
        return ans


nums = [1, 2, 2, 3]
print Solution().permuteUnique(nums)
