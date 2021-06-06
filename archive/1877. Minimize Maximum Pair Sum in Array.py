from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        ans=float("inf")
        while i<j:
            ans=max(nums[i]+nums[j])
            i+=1
            j-=1
        return ans
