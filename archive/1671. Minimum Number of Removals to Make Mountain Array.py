from typing import List
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        longest_inc_seq=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    longest_inc_seq[i]=max(longest_inc_seq[i],longest_inc_seq[j]+1)
        longest_dec_seq = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i,-1):
                if nums[j] < nums[i]:
                    longest_dec_seq[i]=max(longest_dec_seq[i],longest_dec_seq[j]+1)
        print(longest_inc_seq)
        print(longest_dec_seq)
        ans=0
        for i in range(1,len(nums)-1):
            ans=max(ans,longest_inc_seq[i]+longest_dec_seq[i]-1)
        return len(nums)-ans
nums=[9,8,1,7,6,5,4,3,2,1]
print(Solution().minimumMountainRemovals(nums))


