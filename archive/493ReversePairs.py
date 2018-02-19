# coding=utf-8
'''
Created on 2017å¹?10æœ?9æ—?

@author: Administrator
'''


class Solution(object):

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.ans = 0

        def mergeSort(nums):
            mid = len(nums) / 2
            if mid == 0:
                return nums
            left, right = mergeSort(nums[:mid]), mergeSort(nums[mid:])
            i, j = len(left) - 1, len(right) - 1
            while i >= 0 and j >= 0:
                if left[i] > 2 * right[j]:
                    self.ans += j + 1
                    i -= 1
                else:
                    j -= 1
            i = j = 0
            new_nums = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    new_nums.append(left[i])
                    i += 1
                else:
                    new_nums.append(right[j])
                    j += 1
            new_nums += left[i:] + right[j:]
            # print new_nums
            return new_nums

        mergeSort(nums)
        return self.ans


nums = [1, 3, 2, 3, 1]
nums = [2, 4, 3, 5, 1]
print Solution().reversePairs(nums)
