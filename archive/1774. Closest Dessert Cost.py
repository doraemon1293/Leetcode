from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        s = set(baseCosts)

        for top in toppingCosts:
            for x in list(s):
                s.add(x + top)
                s.add(x + top * 2)
        mini = float("inf")
        ans = float("inf")
        for x in s:
            if abs(x - target) <= mini:
                if abs(x-target)==mini:
                    ans = min(ans, x)
                else:
                    ans=x
                mini = abs(x - target)

        return ans


print(Solution().closestCost([5020, 1159],
                             [1253, 5085, 4881, 2593],
                             6819))
