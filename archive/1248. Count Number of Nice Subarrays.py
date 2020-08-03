import collections
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num%2)
        d=collections.defaultdict(int)
        ans=0
        for i in range(prefix):
            ans+=d[prefix[i]-k]
            d[prefix[i]]+=1
        return ans
