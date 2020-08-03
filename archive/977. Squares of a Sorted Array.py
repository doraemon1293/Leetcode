class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A=list(map(lambda x:x**2,A))
        A.sort()
        return A