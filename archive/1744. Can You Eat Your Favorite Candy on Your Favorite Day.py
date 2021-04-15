from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        pre = [0]
        for x in candiesCount:
            pre.append(pre[-1] + x)
        # print(pre)
        for t, day, cap in queries:
            if candiesCount[t] >=1 and cap * (day + 1)>pre[t] and day+1<=pre[t+1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


print(Solution().canEat([7, 4, 5, 3, 8],
                        [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]))
