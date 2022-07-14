from typing import List
import functools


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        K = k
        presum_piles = []
        for pile in piles:
            presum = [0]
            for x in pile:
                presum.append(presum[-1] + x)
            presum_piles.append(presum)

        @functools.lru_cache(None)
        def dp(i, k):
            if i < 0 or k==0:
                return 0
            if k > K or k < 0:
                return -float("inf")
            res = 0
            for j in range(min(len(piles[i]), k) + 1):
                res = max(res, dp(i - 1, k - j) + presum_piles[i][j])
            return res

        return dp(len(piles) - 1, k)


piles = [[1, 100, 3], [7, 8, 9]]
k = 2
print(Solution().maxValueOfCoins(piles, k))
