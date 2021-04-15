from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        pre_min=[None]*len(nums)
        suffix_min=[None]*len(nums)
        pre_min[k]=suffix_min[k]=nums[k]
        for i in range()

