# coding=utf-8
'''
Created on 2017å¹?11æœ?7æ—?

@author: Administrator
'''

# Binary Indexed Tree
# The parent node of right child node index: index-lowbit(index)
# The parent node of left child node index: index+lowbit(index)
# lowbit(index)= (index&-index)


class Bit(object):

    def __init__(self, nums):
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        self.size = len(nums)

    def add(self, index, num):
        while index <= self.size:
            self.bit[index] += num
            index += (index & -index)

    # set arr[index] to num
    def update(self, index, num):
        self.add(index + 1, num - self.bit[index])
        self.nums = num

    # return sum(nums[:index]) (not include nums[index])
    def sum(self, index):
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= (index & -index)

    # return sum(nums[i:j]) (include nums[i] and not include nums[j])
    def sunRange(self, i, j):
        return self.sum(j) - self.sum(i)

