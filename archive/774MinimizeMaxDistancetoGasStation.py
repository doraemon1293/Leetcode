class Solution:

    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        import math
        n = len(stations)
        stations.sort()
        dis = []
        for i in range(n - 1):
            dis.append(stations[i + 1] - stations[i])
        left, right = 0, max(dis)
        while right - left > 0.000001:
            mid = (right + left) / 2
            needed = 0
            for d in dis:
                needed += int(math.ceil(d / mid)) - 1
                if needed > K:
                    break
            if needed > K:
                left = mid
            else:
                right = mid
        return right


stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 9
print(Solution().minmaxGasDist(stations, K))
