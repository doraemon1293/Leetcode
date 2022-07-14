class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length=nums.count(1)
        N=len(nums)
        nums+=nums
        ones=nums[:length].count(1)
        ans=length-ones
        for i in range(1,N):
            ones+=(nums[i+length-1]==1)-(nums[i-1]==1)
            ans=min(ans,length-ones)
        return ans

