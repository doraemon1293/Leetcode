# coding=utf-8
'''
Created on 2017å¹?7æœ?25æ—?

@author: Administrator
'''


class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        st = 0
        while st + 1 < n and nums[st] == nums[st + 1]:
            st += 1
        if n - st <= 2: return n - st
        inc = (nums[st + 1] - nums[st]) > 0
        ans = 2
        last_num = nums[st + 1]
        for num in nums[st + 2:]:
            if inc:
                if num > last_num:
                    last_num = num
                if num < last_num:
                    ans += 1
                    inc = not inc
                    last_num = num
            if not inc:
                if num > last_num:
                    ans += 1
                    inc = not inc
                    last_num = num
                if num < last_num:
                    last_num = num
        return ans


nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
nums = [2, 2, 2, 3]
nums = [3, 3, 3, 2, 5]
print Solution().wiggleMaxLength(nums)
