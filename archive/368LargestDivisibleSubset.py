# coding=utf-8
'''
Created on 2017å¹?7æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse = True)
        arr = []
        last_ind = []
        maxi = -float("inf")
        longestSubset = 0
        tail = -1
        for i in xrange(len(nums)):
            maxi = 0
            for j in xrange(0, i):
                if nums[j] % nums[i] == 0 and arr[j] > maxi:
                    maxi = arr[j]
                    last = j
            if maxi == 0:
                last = -1
            arr.append(maxi + 1)
            last_ind.append(last)
            if maxi + 1 > longestSubset:
                longestSubset = maxi + 1
                tail = i
        ans = []
        while tail != -1:
            ans.append(nums[tail])
            tail = last_ind[tail]
        return ans


nums = [1, 2, 3, 6]
nums = [1, 2, 3]
nums = [1, 2, 4, 8, 10]

print Solution().largestDivisibleSubset(nums)
