# coding=utf-8
'''
Created on 2017å¹?10æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        arr = deque()
        ans = []
        for i, num in enumerate(nums):
            if arr and arr[0][1] < i - k + 1:
                arr.popleft()
            while arr and arr[-1][0] < num:
                arr.pop()
            arr.append((nums[i], i))
            print arr
            if i >= k - 1:
                ans.append(arr[0][0])
        return ans


nums = []
k = 0
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 1
print Solution().maxSlidingWindow(nums, k)

