class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p1,p2,p3):
            x1=p2[0]-p1[0]
            y1=p2[1]-p1[1]
            x2=p3[0]-p1[0]
            y2=p3[1]-p1[1]
            return abs(x1*y2-x2*y1)
        ans=0
        for p1 in points:
            for p2 in points:
                for p3 in points:
                    if area(p1,p2,p3)/2>ans:
                        ans=area(p1,p2,p3)/2
        return ans

