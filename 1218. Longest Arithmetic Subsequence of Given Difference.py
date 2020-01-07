import collections
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        N=len(arr)
        dp=[1]*N
        d=collections.defaultdict(list)
        for i,a in enumerate(arr):
            d[a].append(i)
        for i in range(N):
            temp=arr[i]+difference
            for j in d[temp]:
                dp[j]=max(dp[j],dp[i]+1)
        return max(dp)
