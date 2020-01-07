import bisect


class Solution:
    def jobScheduling(self, startTime: list, endTime: list, profit: list) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]
        for s, e, p in jobs:
            i = bisect.bisect_right(dp, (s, float("inf"))) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append((e, dp[i][1] + p))
        return dp[-1][1]


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
print(Solution().jobScheduling(startTime, endTime, profit))
