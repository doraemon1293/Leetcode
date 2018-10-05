class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = {x: i for i, x in enumerate(A)}
        dp = defaultdict(lambda :2)
        ans=2
        for i,x2 in enumerate(A):
            for j in range(i):
                x1 = A[j]
                k=d.get(x2-x1)
                if k is not None and k < j:
                    dp[i, j] = dp[j, k] + 1
                    ans=max(ans,dp[i, j])
        return ans if ans>=3 else 0