from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        p1=0
        N=len(s)
        ans=0
        while p1<N:
            p2=p1

            while p2<N and s[p2]==s[p1]:
                p2+=1

            if p2>p1:
                maxi = max(cost[p1:p2])
                summ = sum(cost[p1:p2])
                ans+=summ-maxi
            p1=p2
        return ans