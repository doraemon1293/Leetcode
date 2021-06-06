import bisect
from typing import List


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        ans = float("inf")
        pre_sum = [0]
        for size in packages:
            pre_sum.append(pre_sum[-1] + size)

        def summ(i, j):
            return pre_sum[j + 1] - pre_sum[i]

        for supplier in range(len(boxes)):
            boxes[supplier].sort()
            if boxes[supplier][-1] >= packages[-1]:
                wasted = 0
                left = 0
                for size in boxes[supplier]:
                    ind = bisect.bisect_right(packages, size)
                    right = ind - 1
                    if left <= right:
                        wasted += size * (right - left + 1) - summ(left, right)
                    left = right + 1
                    if left >= len(packages):
                        break
                ans = min(wasted, ans)

        return ans % (10 ** 9 + 7) if ans != float("inf") else -1