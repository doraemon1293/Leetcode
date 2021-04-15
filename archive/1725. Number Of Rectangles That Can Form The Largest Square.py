class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxi=max([min(a) for a in rectangles])
        return len([min(a) for a in rectangles if min(a)==maxi])
