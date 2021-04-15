from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans=1
        for num in nums:
            if num==0:
                return 0
            ans=ans*(1 if num>0 else -1)
        return ans
