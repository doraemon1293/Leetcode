# coding=utf-8
'''
Created on 2017å¹?6æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)

        def mergeSort(enums):
            mid = len(enums) / 2
            if mid == 0:
                return enums
            left, right = mergeSort(enums[:mid]), mergeSort(enums[mid:])
            new_enum = []
            while left and right:
                if left[-1][1] > right[-1][1]:
                    ans[left[-1][0]] += len(right)
                    new_enum.append(left.pop())
                else:
                    new_enum.append(right.pop())
            if left:
                new_enum = left + new_enum[::-1]
            elif right:
                new_enum = right + new_enum[::-1]
            else:
                new_enum = new_enum[::-1]
            return new_enum

        mergeSort(list(enumerate(nums)))
        return ans


nums = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]

print Solution().countSmaller(nums)
print nums
