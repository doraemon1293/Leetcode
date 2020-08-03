class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        days = [0] + days
        N = len(days)
        dp = [float("inf")] * N
        dp[0] = 0
        for i in range(1,N):
            for cost, day in zip(costs, [1, 7, 30]):
                j = i
                while j < N and days[j] < days[i] + day:
                    dp[j] = min(dp[j], dp[i-1] + cost)
                    j += 1
            print(dp)
        return dp[-1]


days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(Solution().mincostTickets(days, costs))
