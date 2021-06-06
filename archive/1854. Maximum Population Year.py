from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = []
        maxi = 0
        pop = 0
        for a, b in logs:
            arr.append((a, 1))
            arr.append((b, -1))
        arr.sort()
        for year, p in arr:
            pop += p
            if pop > maxi:
                maxi = pop
                ans = year
        return ans

