class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [startfuel] + [0] * len(stations)
        for i, (dis, fuel) in enumerate(stations):
            for j in range(i,-1,-1):
                if dp[i]>=dis:
                    dp[i+1]=max(dp[i+1],dp[i]+fuel)
        for i,dis in enumerate(dp):
            if dis>=target:
                return i
        return -1

