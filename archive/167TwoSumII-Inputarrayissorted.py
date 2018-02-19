# coding=utf-8
'''
Created on 2016å¹?11æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j and numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        return [i, j]

