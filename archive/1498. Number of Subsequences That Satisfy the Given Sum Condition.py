from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD=10**9+7
        ans=0
        nums.sort()
        pow2=[1]
        for _ in range(len(nums)+1):
            pow2.append((pow2[-1]*2)%MOD)
        l,r=0,len(nums)-1

        while l<=r:
            while r>=l and nums[l]+nums[r]>target:
                r-=1
            if r>=l:
                ans+=pow2[r-l]
            ans%=MOD
            # print(l,r,ans)
            l+=1
        return ans