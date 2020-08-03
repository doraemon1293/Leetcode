import functools


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        summ = [0]
        for stone in stones:
            summ.append(summ[-1] + stone)

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return float("inf")
            if i == j:
                return 0 if m == 1 else float("inf")
            if m == 1:
                return dp(i, j, K) + summ[j + 1] - summ[i]
            return min([dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j)])

        ans=dp(0,n-1,1)
        return -1 if ans==float("inf") else ans

