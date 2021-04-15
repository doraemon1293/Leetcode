import collections
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N=len(nums)
        d=collections.defaultdict(int)
        for i in range(N):
            for j in range(i+1,N):
                d[nums[i]*nums[j]]+=1
        ans=0
        for v in d.values():
            if v>1:
                ans+=v*(v-1)//2
        return ans*8


