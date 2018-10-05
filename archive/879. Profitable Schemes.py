class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        import copy
        dp = [[0] * (G + 1) for _ in range(P + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            new_dp = [row[:] for row in dp]
            for p0 in range(P + 1):
                p1 = min(p0 + p, P)
                for g0 in range(G-g+1):
                    g1 = g0 + g
                    new_dp[p1][g1] += dp[p0][g0]
                    new_dp[p1][g1] %= (10 ** 9 + 7)
            dp=new_dp
        return sum(dp[P])%(10**9+7)
