from typing import List
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def foo(arr):
            return len(arr)==len(set(arr)) and sorted(arr)==arr
        if foo(nums):
            return True
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                if foo(nums[:i]+nums[i+1:]) or foo(nums[:i+1]+nums[i+2:]):
                    return True
                else:
                    return False

