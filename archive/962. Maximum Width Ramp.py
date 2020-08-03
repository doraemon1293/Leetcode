class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(list)

        for i, a in enumerate(A):
            d[a].append(i)

        nums = sorted(d.keys())

        mini = float("inf")
        maxi = -float("inf")
        ans = 0
        for num in nums:
            mini = min(mini, min(d[num]))
            maxi = max(d[num])
            ans = max(maxi - mini, 0, ans)
        return ans
