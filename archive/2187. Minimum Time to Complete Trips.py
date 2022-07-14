import collections


class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        lo = min(time)
        hi = lo * totalTrips

        def foo(mid):
            return sum([mid // t for t in time])

        ans = float("inf")
        while lo <= hi:
            mid = (lo + hi) // 2
            if foo(mid) >= totalTrips:
                ans = min(ans, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return ans



