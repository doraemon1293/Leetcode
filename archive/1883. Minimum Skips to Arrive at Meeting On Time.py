class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        eps = 1e-9

        N = len(dist)
        dp = [0]

        for i in range(len(dist)):
            new_dp = [0] * (N+1)
            d = dist[i]
            new_dp[0] = math.ceil(dp[0] +d/speed-eps)
            for j in range(1, i + 1):
                skip = dp[j - 1] +d/speed
                no_skip = math.ceil(dp[j] +d/speed-eps)
                new_dp[j] = min(skip, no_skip)
            new_dp[i+1]=dp[i] +d/speed
            dp = new_dp

        for i in range(len(dp)):
            if dp[i] <= hoursBefore:
                return i
        return -1