import heapq
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0
        heap = [(0, 0, 0)]
        dp = {(0, 0): 0}
        forbidden = set(forbidden)

        temp=max(forbidden)+a+b
        while heap:
            steps, pos, jump_backward = heapq.heappop(heap)
            # print(steps, pos)
            steps1, pos1 = steps + 1, pos + a
            if pos1 <= temp + x and pos1 not in forbidden:
                if dp.get((pos1, 0), float("inf")) > steps1:
                    heapq.heappush(heap, (steps1, pos1, 0))
                    dp[(pos1, 0)] = steps1
                    if pos1 == x:
                        return steps1
            if jump_backward == 0:
                steps1, pos1 = steps + 1, pos - b
                if pos1 >= 0 and pos1 not in forbidden:
                    if dp.get((pos1, 1), float("inf")) > steps1:
                        heapq.heappush(heap, (steps1, pos1, 1))
                        dp[(pos1, 1)] = steps1
                        if pos1 == x:
                            return steps1
        return -1


print(Solution().minimumJumps(
    [1998],
1999,
2000,
2000,
))
