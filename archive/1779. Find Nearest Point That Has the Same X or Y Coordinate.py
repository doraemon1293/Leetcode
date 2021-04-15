from typing import List
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mini=float("inf")
        ans=-1
        for i, (x1,y1) in enumerate(points):
            if x1==x or y1==y:
                if abs(x-x1)+abs(y-y1)<mini:
                    mini=abs(x-x1)+abs(y-y1)
                    ans=i
        return ans


