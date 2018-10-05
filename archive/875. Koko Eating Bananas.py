import math
class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        lo,hi=1,max(piles)
        def foo(k):
            return sum([int(math.ceil(pile/k)) for pile in piles])
        while lo<hi:
            k=(lo+hi)//2
            if foo(k)>H:
                lo=k+1
            else:
                hi=k
        return lo



