from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=summ=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                summ+=nums[i]
            else:
                summ=nums[i]
            ans=max(ans,summ)
        return ans
