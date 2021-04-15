from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        l=r=summ=0
        ans=0
        while r<len(nums):
            while r<len(nums) and nums[r] not in s:
                s.add(nums[r])
                summ+=nums[r]
                r+=1
            ans=max(ans,summ)
            if r<len(nums):
                while l<len(nums) and nums[l]!=nums[r]:
                    s.remove(nums[l])
                    summ-=nums[l]
                    l+=1
                if l<len(nums):
                    s.remove(nums[l])
                    summ-=nums[l]
                    l+=1
        return ans


