# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        from random import randint
        ans = []
        for i, num in enumerate(self.nums):
            if num == target:
                ans.append(i)
        return ans[randint(0, len(ans) - 1)]


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3, 3, 3])
print obj.pick(3)

#     def __init__(self, nums):
#         """
#
#         :type nums: List[int]
#         :type numsSize: int
#         """
#         self.nums = {}
#
#         for i, num in enumerate(nums):
#             if num in self.nums:
#                 self.nums[num].append(i)
#             else:
#                 self.nums[num] = [i]
#
#
#     def pick(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         from random import randint
#
#         return self.nums[target][randint(0, len(self.nums[target]) - 1)]
