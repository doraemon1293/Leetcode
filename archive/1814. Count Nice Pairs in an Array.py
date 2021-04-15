from typing import List
import collections


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        c = collections.Counter([nums[i] - int(str(nums[i])[::-1]) for i in range(len(nums))])
        return sum(v * (v - 1) // 2 for v in c.values()) % (10**9+7)