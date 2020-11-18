class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points=sorted([point[0] for point in points])
        return max(points[i]-points[i-1] for i in range(1,len(points)))