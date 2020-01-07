from collections import defaultdict


class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """

        dp = dict()
        dp[1] = [1]
        for i in range(2, N + 1):
            dp[i] = [x * 2 - 1 for x in dp[(i+1) // 2]] + [x * 2 for x in dp[i // 2]]
        return dp[N]


N = 100
print(Solution().beautifulArray(N))

#         d=defaultdict(set)
#         for i in range(1,N+1):
#             lo,hi=i-1,i+1
#             while lo>=1 and hi<=N:
#                 d[i].add((lo,hi))
#                 lo-=1
#                 hi+=1
#         print(d)
# N=6
# print(Solution().beautifulArray(N))
