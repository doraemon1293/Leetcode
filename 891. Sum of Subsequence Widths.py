class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        A.sort()
        res = 0
        MOD = 10 ** 9 + 7
        for i, a in enumerate(A):
            res = (res + (1 << i * A[i])) % MOD
            res = (res - (1 << (N - i - 1) * A[i])) % MOD
        return res