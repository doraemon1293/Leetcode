from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = {}
        ans = 0
        for num in nums:
            new_dp = {}
            if num > 0:
                if 1 in dp:
                    new_dp[1] = dp[1] + 1
                if -1 in dp:
                    new_dp[-1] = dp[-1] + 1
                if 1 not in new_dp:
                    new_dp[1]=1

            if num < 0:
                if -1 in dp:
                    new_dp[1] = dp[-1] + 1
                if 1 in dp:
                    new_dp[-1] = dp[1] + 1
                if -1 not in new_dp:
                    new_dp[-1]=1
            dp = new_dp
            # print(dp)

            ans = max(ans, dp.get(1, 0))
        return ans