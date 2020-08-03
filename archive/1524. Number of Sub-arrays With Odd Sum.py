class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp0 = dp1 = 0
        ans = 0
        MOD = 10 ** 9 + 7
        for x in arr:
            if x % 2:
                new_dp1 = dp0 + 1
                new_dp0 = dp1
            else:
                new_dp0 = dp0 + 1
                new_dp1 = dp1

            ans = (ans + new_dp1) % MOD
            dp0, dp1 = new_dp0, new_dp1
        return ans
