# coding=utf-8
'''
Created on 2017å¹?5æœ?25æ—?

@author: Administrator
'''


class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob(st, en, nums):
            if st > en:
                return 0
            elif st == en:
                return nums[st]
            elif st == en - 1:
                return max(nums[st], nums[en])
            else:
                t1 = max(nums[st], nums[st + 1])
                t2 = nums[st]
                for i in range(st + 2, en + 1):
                    ans = max(t1, t2 + nums[i])
                    t2 = t1
                    t1 = ans
                return ans

        if len(nums) < 4:
            return max(nums) if nums else 0
        else:
            return max(rob(0, len(nums) - 2, nums), rob(1, len(nums) - 1, nums))


nums = [1]

print Solution().rob(nums)
