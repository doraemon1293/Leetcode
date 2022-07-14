class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                a,b=nums[i],nums[j]
                if a==b and a*b%k==0:
                    ans+=1
        return ans
