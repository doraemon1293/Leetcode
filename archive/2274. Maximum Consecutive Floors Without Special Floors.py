from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        left = bottom
        p = 0
        ans = 0
        while p < len(special) and special[p] <= top:
            while p < len(special) and special[p] < left:
                p += 1
            if p < len(special):
                right = min(special[p] - 1, top)
            else:
                right = top
            temp = right - left + 1
            ans = max(ans, temp)
            left = right + 2
            # print(p)
        return ans