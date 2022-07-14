class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        inds=[i for i in range(len(nums)) if nums[i]==key]
        ans=set()
        for ind in inds:
            for i in range(max(ind-k,0),min(ind+k+1,len(nums))):
                ans.add(i)
        return sorted(ans)