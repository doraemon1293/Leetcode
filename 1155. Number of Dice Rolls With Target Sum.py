class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        # maxi=0
        for i in range(d):
            new_dp =  [0] * (target + 1)
            for j in range(1, f + 1):
                for k in range(target):
                    if k + j <= target:
                        new_dp[k + j] = (new_dp[k + j] + dp[k]) % (10 ** 9 + 7)
            dp = new_dp[:]
        return dp[target] % (10 ** 9 + 7)
