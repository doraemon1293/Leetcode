# coding=utf-8
'''
Created on 2017�?7�?26�?

@author: Administrator
'''


class Solution(object):

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summ = sum(nums)
        if not nums or summ % 4 or max(nums) > summ / 4: return False
        target = summ / 4
        nums.sort(reverse = True)
        arr = [target] * 4

# 不能用reduce 因为会计算所有�?? 然后TLE
#         def dfs(nums, ind, arr):
#             if ind == len(nums):
#                 return True
#             else:
#                 return reduce(operator.or_, [dfs(nums, ind + 1, [arr[k] - (nums[ind] if k == i else 0) for k in range(4)], target) for i in range(4) if arr[i] >= nums[ind]] + [False])
        def dfs(nums, ind, arr):
            if ind == len(nums):
                return True
            else:
                return (dfs(nums, ind + 1, [arr[k] - (nums[ind] if k == 0 else 0) for k in range(4)]) if arr[0] >= nums[ind] else False) or \
                       (dfs(nums, ind + 1, [arr[k] - (nums[ind] if k == 1 else 0) for k in range(4)]) if arr[1] >= nums[ind] else False) or \
                       (dfs(nums, ind + 1, [arr[k] - (nums[ind] if k == 2 else 0) for k in range(4)]) if arr[2] >= nums[ind] else False) or \
                       (dfs(nums, ind + 1, [arr[k] - (nums[ind] if k == 3 else 0) for k in range(4)]) if arr[3] >= nums[ind] else False)

        # todo 用visited记录arr的状态是True or False缩短搜索时间
        return dfs(nums, 0, arr)


nums = [5, 5, 5, 5, 16, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4]
print Solution().makesquare(nums)

