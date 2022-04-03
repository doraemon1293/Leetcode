class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for x, y, r in queries:
            ans.append(sum([1 for a,b in points if (x-a)**2+(y-b)**2<=r**2]))
        return ans
