from typing import List
import functools


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        M, N = len(pizza), len(pizza[0])
        apples = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                apples[i][j] = apples[i - 1][j] + apples[i][j - 1] - apples[i - 1][j - 1] + (pizza[i - 1][j - 1] == "A")

        dp = {}

        def count_apple(x1, y1, x2, y2):
            return apples[x2 + 1][y2 + 1] - apples[x1][y2 + 1] - apples[x2 + 1][y1] + apples[x1][y1]

        @functools.lru_cache(None)
        def dp(x1, y1, x2, y2, k):
            res = 0
            if count_apple(x1, y1, x2, y2) < k:
                return 0
            if k == 1 and count_apple(x1, y1, x2, y2):
                return 1
            # horizontal
            for x3 in range(x1, x2):
                if count_apple(x1, y1, x3, y2) != 0 and count_apple(x3 + 1, y1, x2, y2) != 0:
                    res += dp(x3 + 1, y1, x2, y2, k - 1)
            # vertical
            for y3 in range(y1, y2):
                if count_apple(x1, y1, x2, y3) != 0 and count_apple(x1, y3 + 1, x2, y2) != 0:
                    res += dp(x1, y3 + 1, x2, y2, k - 1)
            res = res % MOD
            return res

        return dp(0, 0, M - 1, N - 1, k)


pizza = ["A..", "AAA", "..."]
k = 3
pizza = ["A..","A..","..."]
k = 1
print(Solution().ways(pizza, k))
