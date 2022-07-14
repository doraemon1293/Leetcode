import collections
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=collections.Counter(nums)
        ans=0
        for i in range(1,k//2+1):
            j=k-i
            if i!=j:
                ans+=min(c.get(i,0),c.get(j,0))
            else:
                ans+=c.get(i,0)//2
        return ans
