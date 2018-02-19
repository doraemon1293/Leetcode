# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []: return []
        cur_st = cur_en = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] != cur_en + 1:
                if cur_st == cur_en:
                    ans.append(str(cur_st))
                else:
                    ans.append(str(cur_st) + "->" + str(cur_en))
                cur_st = cur_en = nums[i]
            else:
                cur_en += 1

        if cur_st == cur_en:
            ans.append(str(cur_st))
        else:
            ans.append(str(cur_st) + "->" + str(cur_en))
        return ans


nums = [0, 1, 2, 4, 5, 7]
print Solution().summaryRanges(nums)
