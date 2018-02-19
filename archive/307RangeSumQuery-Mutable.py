# coding=utf-8
'''
Created on 2017å¹?11æœ?7æ—?

@author: Administrator
'''

# coding=utf-8
'''
Created on 2017å¹?8æœ?18æ—?

@author: Administrator
'''


class NumArray(object):

    def __init__(self, nums):
        self.nums = [0] * len(nums)
        self.tree = [0] * (len(nums) + 1)
        self.size = len(nums)
        for i, num in enumerate(nums):
            self.update(i, num)

    # set arr[index] to num
    def update(self, i, val):
        index = i + 1
        delta = val - self.nums[i]
        while index <= self.size:
            self.tree[index] += delta
            index += (index & -index)
        self.nums[i] = val

    # return sum(nums[:index]) (not include nums[index])
    def sum(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= (index & -index)
        return res

    # return sum(nums[i:j+1])
    def sumRange(self, i, j):
        return self.sum(j + 1) - self.sum(i)

# class NumArray(object):
#
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#
#
#     def update(self, i, val):
#         """
#         :type i: int
#         :type val: int
#         :rtype: void
#         """
#
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

