from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        nums = [0] + nums + [0]
        a = b = c=None
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if a == None:
                    a = i
                elif b == None:
                    b = i
                else:
                    c=i
                    length = (c - a + 1) - 3
                    ans = max(ans, length)
                    a, b = b, c
        if c==None:
            return len(nums)-2-1
        return ans