class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, a in enumerate(A):
            if a==i:
                return i
        return -1