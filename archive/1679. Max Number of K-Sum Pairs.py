import collections
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=collections.defaultdict(int)
        ans=0
        for num in nums:
            d[num]+=1
            if num*2==k:
                if d[k-num]>=2:
                    d[k-num]-=2
                    ans+=1
            else:
                if d[k-num]:
                    d[num]-=1
                    d[k-num]-=1
                    ans+=1
        return ans

nums=[1,2,3,4]
k=5

print(Solution().maxOperations(nums,k))