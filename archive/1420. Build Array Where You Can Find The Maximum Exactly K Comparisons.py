from functools import lru_cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10**9+7
        @lru_cache(None)
        def dp(n, largest, k):
            if n == 1:
                return 1 if k == 1 else 0
            if k == 0:
                return 0
            res = 0
            res += dp(n - 1, largest, k) * largest
            for num in range(1, largest):
                res += dp(n - 1, num, k - 1)
            res = res % MOD
            return res

        return sum(dp(n, i, k) for i in range(1, m + 1)) % MOD


n = 50
m = 100
k = 25
print(Solution().numOfArrays(n, m, k))
