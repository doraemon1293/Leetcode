class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left=A[0]
        ans=-float("inf")
        for a in A:
            left-=1
            ans=max(left+a,ans)
            left=max(a,left)
        return ans


