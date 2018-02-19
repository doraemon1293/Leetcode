# coding=utf-8
'''
Created on 2017å¹?10æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sums = []
        temp = sum(nums[:k])
        sums.append(temp)
        for i in xrange(1, len(nums) - k + 1):
            temp += nums[i + k - 1] - nums[i - 1]
            sums.append(temp)
        max_left = [[0, -1] for _ in xrange(len(sums))]
        maxi = 0
        ind = -1
        for i in xrange(len(sums)):
            if sums[i] > maxi:
                maxi = sums[i]
                ind = i
            max_left[i][0], max_left[i][1] = maxi, ind
        max_right = [[0, -1] for _ in xrange(len(sums))]
        maxi = 0
        ind = -1

        for i in xrange(len(sums) - 1, -1, -1):
            if sums[i] > maxi:
                maxi = sums[i]
                ind = i
            if sums[i] == maxi:
                ind = i
            max_right[i][0], max_right[i][1] = maxi, ind
        ans = 0
        arr = [0, 0, 0]
        for mid in xrange(k, len(sums) - k):
            temp = max_left[mid - k][0] + sums[mid] + max_right[mid + k][0]
            if temp > ans:
                ans = temp
                arr = [max_left[mid - k][1], mid, max_right[mid + k][1]]
            elif temp == ans:
                if [max_left[mid - k][1], mid, max_right[mid + k][1]] < arr:
                    arr = [max_left[mid - k][1], mid, max_right[mid + k][1]]
        return arr


nums = [1, 2, 1, 2, 6, 7, 5, 1]
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
k = 2
print Solution().maxSumOfThreeSubarrays(nums, k)
