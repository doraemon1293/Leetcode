from collections import defaultdict


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        succ = {1: [6, 8],
                2: [7, 9],
                3: [4, 8],
                4: [3, 9, 0],
                5: [],
                6: [1, 7, 0],
                7: [2, 6],
                8: [1, 3],
                9: [2, 4],
                0: [4, 6],
                }
        dp = [1] * 10
        for _ in range(N - 1):
            new_dp = [None] * 10
            for i in range(10):
                new_dp[i] = sum(dp[j] for j in succ[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD

N=5000
print(Solution().knightDialer(N))