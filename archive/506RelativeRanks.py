# coding=utf-8
'''
Created on 2017å¹?2æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = [None] * len(nums)
        arr = list(enumerate(nums))
        arr.sort(key = lambda x:x[1], reverse = True)
        print arr
        for i in range(len(arr)):
            ans[arr[i][0]] = str(i + 1) if i > 2 else ["Gold Medal", "Silver Medal", "Bronze Medal"][i]
        return ans


nums = [5, 4, 3, 2, 1]
print Solution().findRelativeRanks(nums)

