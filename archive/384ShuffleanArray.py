# coding=utf-8
'''
Created on 2016å¹?11æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        import copy
        self.nums = nums
        self.arr = copy.copy(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        import copy
        self.arr = copy.copy(self.nums)
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        random.shuffle(self.arr)
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
