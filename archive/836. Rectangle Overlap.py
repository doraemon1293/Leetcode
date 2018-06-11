class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x_overlap=max(0,min(rec2[2],rec1[2])-max(rec2[0],rec1[0]))
        y_overlap=max(0,min(rec2[3],rec1[3])-max(rec2[1],rec1[1]))
        return x_overlap*y_overlap>0
