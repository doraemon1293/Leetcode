class Solution:
    def minFallingPathSum(self, arr: list) -> int:
        pass
        dp=[arr[0]]
        for a in arr[1:]:
            new_dp=[float("inf")]*len(a)
            for i in range(len(a)):
                new_dp[i]=min(dp[:i]+dp[i+1:])+a[i]
            dp=new_dp
        return min(dp)

