from typing import List
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        max_day = max([i + days[i] for i in range(len(days))])
        cur = 0
        heap = []
        ans = 0
        for i in range(max_day):
            # rotten
            while heap and (heap[0][0] == i or heap[0][1] == 0):
                heapq.heappop(heap)

            if i < len(apples):
                a, b = apples[i], days[i]
                if a != 0:
                    # rot in future
                    heapq.heappush(heap, [i + days[i], a])
            # eat one
            if heap:
                heap[0][1] -= 1
                if heap[0][1] == 0:
                    heapq.heappop(heap)
                ans += 1
        return ans