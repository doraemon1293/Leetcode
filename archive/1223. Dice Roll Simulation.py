import collections


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        rollMax = [float("inf")] + rollMax
        dp = {(0, 0): 1}
        mod = 10 ** 9 + 7
        for _ in range(n):
            new_dp = collections.defaultdict(int)
            for i in range(1, 7):
                for dice, times in dp:
                    v = dp[dice, times]
                    if i == dice:
                        if times < rollMax[dice]:
                            new_dp[dice, times + 1] += v
                    else:
                        new_dp[i, 1] += v
            dp = dict([(k, v % mod) for k, v in new_dp.items()])
        return sum(dp.values()) % mod
