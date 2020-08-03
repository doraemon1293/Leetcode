import heapq


class Solution:

    def maxEvents(self, events: list) -> int:
        events.sort(reverse=1)
        h = []
        ans = 0
        for d in range(1, 100001):
            while events and events[-1][0] == d:
                heapq.heappush(h, events.pop()[1])
            while h and h[0] < d:
                heapq.heappop(h)
            if h:
                heapq.heappop(h)
                ans += 1
        return ans
