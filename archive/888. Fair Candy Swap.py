class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a=sum(A)
        sum_b=sum(B)
        set_a=set(A)
        for bi in B:
            if (sum_a-sum_b)//2+bi in set_a:
                return [(sum_a-sum_b)//2+bi,bi]