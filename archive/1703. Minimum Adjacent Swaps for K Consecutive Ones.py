from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        nums=[i for i,num in enumerate(nums) if num==1]
        nums=[x-i for i,x in enumerate(nums)]
        N=len(nums)
        summ=0
        for num in nums[:k]:
            summ+=abs(num-nums[k//2])
        ans=summ

        for right in range(k,N):
            left=right-k+1
            median_ind=(right+left)//2
            old_median_ind=median_ind-1
            if k%2:
                summ+=(nums[right]-nums[median_ind])-(nums[old_median_ind]-nums[left-1])
            else:
                summ+=(nums[right]-nums[median_ind])-(nums[old_median_ind]-nums[left-1]+nums[median_ind]-nums[old_median_ind])
            ans=min(ans,summ)
        return ans


print(Solution().minMoves(nums = [1,1,0,1], k = 2)
)