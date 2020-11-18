from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def sum_(n, k):
            # print("sum", n, k)
            if n <= k:
                return 0
            else:
                return (sum_(n - 1, k) + dp(n, k)) % MOD

        @lru_cache(None)
        def dp(n, k):
            # print(n, k)
            if k == 0:
                return 1
            if n - 1 == k:
                return 1
            if n - 1 < k:
                return 0
            return (sum_(n-1, k - 1) + dp(n - 1, k)) % MOD

        return dp(n, k)


# print(Solution().numberOfSets(n = 30, k =7))
print(Solution().numberOfSets(n=633, k=64))
