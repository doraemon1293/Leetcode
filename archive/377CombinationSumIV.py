# coding=utf-8
'''
Created on 2016å¹?11æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        d = {}

        def dfs(sum):
            ans = 0
            if sum in d:
                return d[sum]
            for num in nums:
                print num, sum
                # raw_input()
                if num > sum:
                    break
                if num == sum:
                    ans += 1
                else:
                    ans += dfs(sum - num)
            d[sum] = ans
            return ans

        return dfs(target)


nums = [4, 2, 1]
target = 32
print Solution().combinationSum4(nums, target)

