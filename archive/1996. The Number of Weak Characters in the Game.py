from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True)
        maxi_def = 0
        ans = 0
        p1 = 0
        p2 = 0
        while p2 < len(properties):
            while p2 < len(properties) and (p2 == p1 or properties[p2][0] == properties[p2 - 1][0]):
                if properties[p2][1] < maxi_def:
                    ans += 1
                p2 += 1

            while p1 < p2:
                maxi_def = max(maxi_def, properties[p1][1])
                p1 += 1

        return ans

p=[[1,1],[2,1],[2,2],[1,2]]
print(Solution().numberOfWeakCharacters(p))