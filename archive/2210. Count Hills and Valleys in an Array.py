class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans=0
        left_nbr=nums[0]
        for i in range(1,len(nums)-1):
            if nums[i]==left_nbr:
                pass
            elif nums[i]==nums[i+1]:
                pass
            else:
                if nums[i]>left_nbr and nums[i]>nums[i+1]:
                    ans+=1
                    left_nbr=nums[i]
                elif nums[i]<left_nbr and nums[i]<nums[i+1]:
                    ans+=1
                    left_nbr=nums[i]
        return ans
