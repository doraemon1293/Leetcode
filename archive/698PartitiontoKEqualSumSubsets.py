# coding=utf-8
'''
Created on 2017å¹?10æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        summ = sum(nums)
        if summ % k != 0: return False
        target = summ / k
        if max(nums) > target:
            return False
        used = [False] * len(nums)
        nums = sorted(nums, reverse = True)
        memo = set()

        def dfs(cur_target, k, nums, used, st,):
            # print cur_target, k, nums, used, st
            key = (cur_target, k)
            if key in memo:
                return False
            if k == 1:
                return True
            if cur_target == 0:
                if dfs(target, k - 1, nums, used, 0):
                    return True
                else:
                    memo.add(key)
            for i in range(st, len(nums)):
                if used[i] == False and nums[i] <= cur_target:
                    used[i] = True
                    if dfs(cur_target - nums[i], k, nums, used, i + 1):
                        return True
                    used[i] = False
                    if dfs(cur_target, k, nums, used, i + 1):
                        return True
            memo.add(key)
            return False

        return dfs(target, k, nums, used, 0)


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
nums = [2, 2, 2, 2, 3, 4, 5]
nums = [3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269]
k = 5
print Solution().canPartitionKSubsets(nums, k)

