from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[::]
        q = deque()
        for i in range(len(nums)):
            if q and q[0][1] < i - k:
                q.popleft()
            maxi = max(q[0][0] if q else 0,0)
            dp[i] = maxi + nums[i]
            while q and q[-1][0] < dp[i]:
                q.pop()
            q.append((dp[i], i))
        # print(dp)
        return max(dp)
nums=[-5266,4019,7336,-3681,-5767]
k=2
print(Solution().constrainedSubsetSum(nums,k))